import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# -------------------------------
# Load and prepare data
# -------------------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

# -------------------------------
# Model builder
# -------------------------------
def build_model(activation):
    model = models.Sequential([
        layers.Flatten(input_shape=(28, 28)),
        layers.Dense(128, activation=activation),
        layers.Dense(64, activation=activation),
        layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

# -------------------------------
# Train and save models
# -------------------------------
Activations = ["relu", "sigmoid", "tanh"]

for act in Activations:
    print(f"\nTraining model with activation: {act}")

    Mdl = build_model(act)
    Mdl.fit(
        x_train,
        y_train,
        epochs=5,
        validation_split=0.2,
        verbose=1
    )

    Save_Path = f"Lesson 2/l2_mdl_{act}.h5"
    Mdl.save(Save_Path)

    print(f"Saved: {Save_Path}")
