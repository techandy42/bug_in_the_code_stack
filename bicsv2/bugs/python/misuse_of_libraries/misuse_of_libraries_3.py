import tensorflow as tf

def train_model(epochs, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile_model(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    x_train = tf.random.normal((1000, 10))
    y_train = tf.random.uniform((1000,), minval=0, maxval=2, dtype=tf.int32)

    history = model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)
    return history
