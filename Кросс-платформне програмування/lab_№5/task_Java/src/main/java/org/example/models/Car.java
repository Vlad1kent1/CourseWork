package org.example.models;

public class Car extends Transport {
    private String model;
    private int year;

    public Car(int speed, int capacity, String fuelType, String model, int year) {
        super(speed, capacity, fuelType);
        this.model = model;
        this.year = year;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    @Override
    public void move() {
        System.out.println("Car is moving.");
    }

    @Override
    public String displayInfo() {
        return "Car: {model: " + model + ", year: " + getYear() + ", speed: " + getSpeed() + ", capacity: " + getCapacity() + ", fuel type: " + getFuelType() + "}";
    }
}
