import pandas as pd

df_ds = pd.read_csv('../../datasets/bug_in_the_code_stack_alpaca_dataset.csv')
string_columns = df_ds.select_dtypes(include=['object']).columns
df_ds[string_columns] = df_ds[string_columns].fillna('')

from abc import ABC, abstractmethod

class Tokenizer(ABC):
    def __init__(self, *args, **kwargs):
        """
        Initialize the Tokenizer with any number of arguments.

        Parameters:
        *args: A tuple of positional arguments.
        **kwargs: A dictionary of keyword arguments.
        """
        # You can handle or pass these arguments as needed
        super().__init__(*args, **kwargs)  # Optional: useful if extending another class with an __init__

    @abstractmethod
    def count_tokens(self, string: str) -> int:
        """
        Abstract method to count tokens in a string.

        Parameters:
        string (str): The string to count tokens in.

        Returns:
        int: The number of tokens.
        """
        pass

import tiktoken

class GeminiTokenizer(Tokenizer):
  def __init__(self, encoding_name):
    self.encoding_name = encoding_name

  def count_tokens(self, string: str) -> int:
      """Returns the number of tokens in a text string."""
      encoding = tiktoken.get_encoding(self.encoding_name)
      num_tokens = len(encoding.encode(string))
      return num_tokens

import os

tokenizer = GeminiTokenizer("cl100k_base")

def number_lines(input_string):
    lines = input_string.splitlines()  # Split the string into lines
    total_lines = len(lines)  # Get the total number of lines to determine the padding width
    max_width = len(str(total_lines))  # Width of the largest line number

    # Enumerate over lines, start counting from 1, and left-align the line numbers
    numbered_lines = [f"{i+1:<{max_width}}| {line}" for i, line in enumerate(lines)]
    # Join the modified lines back into a single string with newlines
    return "\n".join(numbered_lines)

import pandas as pd
import numpy as np

def build_bug_string(df, tokenizer, target_length, target_depth, target_bug):
    selected_strings = []
    total_tokens = 0

    # Randomly select initial strings until target_depth
    while total_tokens < target_length * target_depth:
        row = df['output'].sample().iloc[0]
        selected_strings.append(row)
        total_tokens = tokenizer.count_tokens(number_lines('\n\n'.join(selected_strings)))

    # Remove the last string if we've exceeded the target depth
    if total_tokens > target_length * target_depth:
        selected_strings.pop()
        total_tokens = tokenizer.count_tokens(number_lines('\n\n'.join(selected_strings)))

    # Insert a bug string
    bug_column = f'output_{target_bug}'
    bug_lines_column = f'bug_line_number_{target_bug}'

    # Filter non-empty bug strings and sample one
    bug_df = df[df[bug_column] != ""]
    if bug_df.empty:
        raise ValueError("No entries found for the specified bug type.")
    bug_row = bug_df.sample()
    bug_string = bug_row[bug_column].iloc[0]
    bug_line_number = bug_row[bug_lines_column].iloc[0]
    selected_strings.append(bug_string)
    bug_index = len(selected_strings) - 1  # Index of the bug string in the list

    # Continue adding until just below target_length
    while total_tokens < target_length:
        row = df['output'].sample().iloc[0]
        selected_strings.append(row)
        total_tokens = tokenizer.count_tokens(number_lines('\n\n'.join(selected_strings)))
        if total_tokens >= target_length:
            selected_strings.pop()  # Remove last added string if over limit
            break

    # Concatenate all strings
    result_string = number_lines('\n\n'.join(selected_strings))

    # Calculate bug line number
    result_string_before_bug = number_lines('\n\n'.join(selected_strings[:bug_index]))
    num_lines_before_bug = result_string_before_bug.count('\n')
    bug_line_number_from_start = num_lines_before_bug + bug_line_number
    if len(selected_strings[:bug_index]) > 0:
      bug_line_number_from_start += 2  # Add 2 for the newlines before the string with bug

    return result_string, bug_line_number_from_start, target_bug

"""> Bug Types

- `missing_colon`
- `missing_parenthesis`
- `missing_quotation`
- `missing_comma`
- `mismatched_quotation`
- `mismatched_bracket`
- `keywords_as_identifier`
"""

background_code, bug_line_number, bug_type = build_bug_string(df_ds, tokenizer, 200, 0.75, 'missing_parenthesis')
print('Auto-Generated Code Background w/t Bug:')
print(background_code)
print()
print('Bug Line Number:')
print(bug_line_number)
print()
print('Bug Type:')
print(bug_type)

def generate_prompt(background_code):
  prompt = f"""<system>
You are a intelligent assistant.
</system>
  
I will give you a codebase with a syntactic bug hidden at some line. You need to answer the line at which the syntactic error occurs and the type of the syntactic error.

<example>
1 | def fahrenheit_to_celsius(fahrenheit):
2 |   return (fahrenheit - 32) * 5.0/9.0
3 |
4 | def is_prime(num:
5 |     if num <= 1:
6 |         return False
7 |     for i in range(2, int(num**0.5) + 1):
8 |         if num % i == 0:
9 |             return False
10|     return True
Answer: 4, missing_parenthesis
</example>

<example>
1| import random
2| import string
3|
4| def generate_password(length=8):
5|     characters = string.ascii_letters + string.digits
6|     password = '\".join(random.choice(characters) for i in range(length))
7|     return password
Answer: 6, mismatched_quotation
</example>

<context>
{background_code}
</context>

<bug_types>
missing_colon
missing_parenthesis
missing_quotation
missing_comma
mismatched_quotation
mismatched_bracket
keywords_as_identifier
</bug_types>

Always return your answer in the following format: <line_number>, <bug_type>
Do not write anything else after that."""

  return prompt

print(generate_prompt(background_code))

from abc import ABC, abstractmethod
from typing import Tuple

class Model(ABC):
    def __init__(self, *args, **kwargs):
        """
        Initialize the Tokenizer with any number of arguments.

        Parameters:
        *args: A tuple of positional arguments.
        **kwargs: A dictionary of keyword arguments.
        """
        # You can handle or pass these arguments as needed
        super().__init__(*args, **kwargs)  # Optional: useful if extending another class with an __init__

    @abstractmethod
    def ask_single_bug_test(self, prompt: str) -> Tuple[int, str]:
        """
        Abstract method to ask single bug test to the model.

        Parameters:
        prompt (str): The single bug test prompt.

        Returns:
        int: The line number of the bug.
        str: The type of the bug.
        """
        pass

    @abstractmethod
    def get_context_limit(self) -> int:
        """
        Abstract method to get the context limit of the model.

        Returns:
        int: The context limit.
        """
        pass

import google.generativeai as genai
from typing import Tuple
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiModel(Model):
    def __init__(self, model_name, context_limit):
      genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
      self.model_name = model_name
      self.context_limit = context_limit

    def ask_single_bug_test(self, prompt: str) -> Tuple[int, str]:
      model = genai.GenerativeModel(self.model_name)
      response = model.generate_content(prompt)
      answer = response.text.strip().lower()

      if answer.endswith('.'):
          answer = answer[:-1]

      line_number, bug_type = answer.split(',')
      line_number = int(line_number.strip())
      bug_type = bug_type.strip()

      return line_number, bug_type

    def get_context_limit(self) -> int:
      return self.context_limit

model_name = "gemini-1.0-pro"
context_limit = 128000

model = GeminiModel(model_name, context_limit)

from datetime import datetime

def get_unique_time_string():
    current_time = datetime.now()
    return current_time.strftime("%Y%m%d%H%M%S%f")

import os

def create_directory_if_not_exists(path, verbose=False):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                print(f"Directory created at: {path}")
        else:
            if verbose:
                print(f"Directory already exists at: {path}")
    except OSError as error:
        if verbose:
            print(f"Error creating directory at {path}: {error}")

import random
import pandas as pd
import time

def single_bug_test(df, tokenizer, model, target_lengths, target_depths, num_iter, verbose=False):
    outfile = f'single_bug_test/result_{get_unique_time_string()}.csv'
    create_directory_if_not_exists('single_bug_test', verbose)

    bug_types = [
        'missing_colon',
        'missing_parenthesis',
        'missing_quotation',
        'missing_comma',
        'mismatched_quotation',
        'mismatched_bracket',
        'keywords_as_identifier'
    ]

    test_no = 1

    df_test_result = pd.DataFrame({
        'target_length': [],
        'target_depth': [],
        'iter_no': [],
        'bug_line_number': [],
        'bug_type': [],
        'pred_bug_line_number': [],
        'pred_bug_type': [],
        'result': [],
    })

    for target_length in target_lengths:
        for target_depth in target_depths:
            i = 0
            while i < num_iter:
                error_count = 0  # Counter for the number of consecutive errors
                while error_count < 3:
                    time.sleep(2)  # Sleep for 2 seconds between iterations
                    
                    try:
                        background_code, bug_line_number, bug_type = build_bug_string(df, tokenizer, target_length, target_depth, random.choice(bug_types))
                        prompt = generate_prompt(background_code)
                        prompt_token_count = tokenizer.count_tokens(prompt)

                        if prompt_token_count > model.get_context_limit():
                            if verbose:
                                print(f"Prompt token count {prompt_token_count} exceeds context limit {model.get_context_limit()}. Skipping.")
                            break  # Exit the error handling loop and skip to the next iteration

                        pred_bug_line_number, pred_bug_type = model.ask_single_bug_test(prompt)
                        pred_correct = pred_bug_line_number == bug_line_number and pred_bug_type == bug_type

                        df_test_result.loc[len(df_test_result)] = [target_length, target_depth, i, bug_line_number, bug_type, pred_bug_line_number, pred_bug_type, pred_correct]
                        df_test_result.to_csv(outfile, index=False)

                        if verbose:
                            print("=" * 30)
                            print(f"Test {test_no} (target length: {target_length}, target depth: {target_depth}):")
                            print(f"Actual bug line number: {bug_line_number}, actual bug type: {bug_type}")
                            print(f"Predicted bug line number: {pred_bug_line_number}, predicted bug type: {pred_bug_type}")
                            print(f"{'Correct Prediction' if pred_correct else 'Wrong Prediction'}")
                            print("=" * 30)

                        test_no += 1
                        error_count = 0  # Reset the error count after a successful attempt
                        break  # Exit the error handling loop

                    except Exception as e:
                        error_count += 1  # Increment the error counter
                        if verbose:
                            print(f"Error in test {test_no} (attempt {error_count}, target length: {target_length}, target depth: {target_depth}): {e}")
                        if error_count >= 3:
                            # If 3 errors have occurred, log it and move on to the next i
                            if verbose:
                                print(f"Three consecutive errors occurred for iteration {i}. Moving on to the next iteration.")
                            break  # Break out of the loop after 3 errors

                if error_count < 3:
                    # Only increment i if we didn't break due to errors exceeding the limit
                    i += 1

single_bug_test(df_ds, tokenizer, model, [500, 1000, 2000, 4000, 8000, 15500], [0, 0.25, 0.5, 0.75, 1], 25, True)

import os
from datetime import datetime

def find_latest_file(directory):
    # Define the directory path
    dir_path = os.path.abspath(directory)

    # Initialize variables to track the latest file
    latest_file = None
    latest_time = None

    # Iterate through all files in the directory
    for filename in os.listdir(dir_path):
        # Extract the timestamp from the filename
        timestamp_str = filename.split('_')[1].split('.')[0]
        try:
            # Convert the timestamp string to a datetime object
            timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
            # Update the latest file if this file is newer
            if latest_time is None or timestamp > latest_time:
                latest_time = timestamp
                latest_file = filename
        except ValueError:
            # Skip files that do not match the expected format
            continue

    # Return the latest file found, or None if no valid file was found
    return latest_file if latest_file else None

import os

# Replace with hard-coded path to specify a different experiment result
outfile_path = os.path.join('single_bug_test', find_latest_file('single_bug_test'))
print(f"Outfile Path: {outfile_path}")
