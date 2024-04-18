package org.example.carparking.controller;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import org.example.carparking.CarParkingDAO;
import org.example.carparking.data.CarParking;

import java.util.List;

public class CheckDebtorsController {
    public TextField currentHourInput;
    public ListView debtorsList;

    private Stage stage;
    private MainController mainController;

    public void setStage(Stage newWindow) {
        stage = newWindow;
    }

    public void setMainController(MainController mainController) {
        this.mainController = mainController;
    }

    public void onCheckButtonPress(ActionEvent actionEvent) {
        int hour = Integer.parseInt(currentHourInput.getText());
        List<CarParking> carParkingList = CarParkingDAO.getAll();
        ObservableList<CarParking> ol = FXCollections.observableArrayList();
        for (CarParking carParking : carParkingList) {
            if (Math.abs(hour - carParking.getParking_hour()) < carParking.getPrepaid_hours()) {
                ol.add(carParking);
            }
        }
        debtorsList.setItems(ol);
    }
}
