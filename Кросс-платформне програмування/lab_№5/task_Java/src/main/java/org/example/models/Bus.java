package org.example.models;

public class Bus extends Transport {
    private int numberOfSeats;

    public Bus(int speed, int capacity, String fuelType, int numberOfSeats) {
        super(speed, capacity, fuelType);
        this.numberOfSeats = numberOfSeats;
    }

    public int getNumberOfSeats() {
        return numberOfSeats;
    }

    public void setNumberOfSeats(int numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }

    @Override
    public void move() {
        System.out.println("Bus is moving.");
    }

    @Override
    public String displayInfo() {
        System.out.println("Number of Seats: " + numberOfSeats);
        System.out.println("Speed: " + getSpeed());
        System.out.println("Capacity: " + getCapacity());
        System.out.println("Fuel Type: " + getFuelType());
        return "Motorcycle: {number of seats: " + numberOfSeats + ", speed: " + getSpeed() + ", capacity: " + getCapacity() + ", fuel type: " + getFuelType() + "}";
    }
}

