package org.example.carparking.repository;

import org.example.carparking.data.CarParking;

import java.util.List;

public class CarParkingRepository implements Repository{

    @Override
    public List<CarParking> getAll() {
        return null;
    }

    @Override
    public CarParking getById(int id) {
        return null;
    }

    @Override
    public List<CarParking> getAllByBrand(String brand) {
        return null;
    }

    @Override
    public boolean addCarParking(CarParking CarParking) {
        return false;
    }

    @Override
    public boolean updateCarParking(int id, CarParking CarParking) {
        return false;
    }

    @Override
    public boolean deleteCarParking(int id) {
        return false;
    }
}
