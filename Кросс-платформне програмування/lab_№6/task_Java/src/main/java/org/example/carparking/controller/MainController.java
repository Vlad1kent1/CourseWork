package org.example.carparking.controller;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ListView;
import javafx.stage.Stage;
import org.example.carparking.CarParkingDAO;
import org.example.carparking.CarParkingManager;
import org.example.carparking.data.CarParking;

import java.io.IOException;
import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

public class MainController implements Initializable {

    public ListView carParkingList;

    @FXML
    public void onAddButtonPress(ActionEvent actionEvent) {
        FXMLLoader loader =
                new FXMLLoader(CarParkingManager.class.getResource("add-carparking-view.fxml"));
        Stage newWindow = newStage("Add CarParking", loader);
        AddCarParkingController newController = loader.getController();
        newController.setStage(newWindow);
        newController.setMainController(this);
        newWindow.show();
    }

    public void onCheckByLicensePlateButtonPress(ActionEvent actionEvent) {
        FXMLLoader loader =
                new FXMLLoader(CarParkingManager.class.getResource("check-by-license-plate-view.fxml"));
        Stage newWindow = newStage("Check By License Plate", loader);
        CheckByLicensePlateController newController = loader.getController();
        newController.setStage(newWindow);
        newController.setMainController(this);
        newWindow.show();
    }

    public void onCheckDebtorsButtonPress(ActionEvent actionEvent) {
        FXMLLoader loader =
                new FXMLLoader(CarParkingManager.class.getResource("check-debtors-view.fxml"));
        Stage newWindow = newStage("Check Debtors", loader);
        CheckDebtorsController newController = loader.getController();
        newController.setStage(newWindow);
        newController.setMainController(this);
        newWindow.show();
    }

    public void onUpdateButtonPress(ActionEvent actionEvent) {
        CarParking updatedCarParking = (CarParking) carParkingList.getSelectionModel().getSelectedItem();
        FXMLLoader loader =
                new FXMLLoader(CarParkingManager.class.getResource("update-carparking-view.fxml"));
        Stage newWindow = newStage("Update CarParking", loader);
        UpdateCarParkingController newController = loader.getController();
        newController.initData(updatedCarParking);
        newController.setStage(newWindow);
        newController.setMainController(this);
        newWindow.show();
    }

    public void onDeleteButtonPress(ActionEvent actionEvent) {
        CarParking deletedCarParking = (CarParking) carParkingList.getSelectionModel().getSelectedItem();
        CarParkingDAO.deleteCar(deletedCarParking);
        refresh();
    }

    private Stage newStage(String title, FXMLLoader loader) {
        Stage newWindow = new Stage();
        Parent root = null;
        try {
            root = loader.load();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        newWindow.setTitle(title);
        newWindow.setScene(new Scene(root));
        return newWindow;
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        List<CarParking> carParkings = CarParkingDAO.getAll();
        ObservableList<CarParking> ol = FXCollections.observableList(carParkings);
        ol.add(null);
        refresh();
    }

    public void refresh() {
        List<CarParking> carParking = CarParkingDAO.getAll();
        ObservableList<CarParking> carParkingOl = FXCollections.observableList(carParking);
        carParkingList.setItems(carParkingOl);
    }
}