import pyroomacoustics as pra
import matplotlib.pyplot as plt

def main():
    room = pra.ShoeBox(
        [5, 5, 3],
        fs=48000,
        materials=pra.Material(0.3),
        max_order=10
    )

    # Speaker location
    room.add_source([2.5, 2.5, 1.2])
        
    # Single microphone
    room.add_microphone(
        [
            [2.6],
            [2.5],
            [1.2]
        ]
    )

    fig, ax = room.plot()
    ax.set_title("AcouSim Room Visualization")
    plt.show()

if __name__ == "__main__":
    main()