package org.example.models;

import java.awt.*;
import java.io.Serializable;

public abstract class Transport implements Serializable {
    private int speed;
    private int capacity;
    private String fuelType;

    public Transport(int speed, int capacity, String fuelType) {
        this.speed = speed;
        this.capacity = capacity;
        this.fuelType = fuelType;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public String getFuelType() {
        return fuelType;
    }

    public void setFuelType(String fuelType) {
        this.fuelType = fuelType;
    }

    public abstract void move();

    public abstract String displayInfo();
}

