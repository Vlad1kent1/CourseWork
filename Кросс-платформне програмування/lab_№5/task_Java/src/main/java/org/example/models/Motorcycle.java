package org.example.models;

public class Motorcycle extends Transport {
    private String type;

    public Motorcycle(int speed, int capacity, String fuelType, String type) {
        super(speed, capacity, fuelType);
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    @Override
    public void move() {
        System.out.println("Motorcycle is moving.");
    }

    @Override
    public String displayInfo() {
        return "Motorcycle: {type: " + type + ", speed: " + getSpeed() + ", capacity: " + getCapacity() + ", fuel type: " + getFuelType()  + "}";
    }
}

