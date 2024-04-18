package org.example.carparking.repository;

import org.example.carparking.data.CarParking;

import java.util.List;

public interface Repository {
    List<CarParking> getAll();
    CarParking getById(int id);
    List<CarParking> getAllByBrand(String brand);
    boolean addCarParking(CarParking CarParking);
    boolean updateCarParking(int id, CarParking CarParking);
    boolean deleteCarParking(int id);
}
