package org.example;

import org.example.models.Player;
import org.example.models.Bus;
import org.example.models.Car;
import org.example.models.Motorcycle;
import org.example.models.Transport;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class Main extends JFrame {
    private DefaultListModel<Player> playerListModel;
    private JList<Player> playerList;

    public Main() {
        setTitle("Transport Game");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);
        setLocationRelativeTo(null);

        // Ініціалізуємо список гравців
        playerListModel = new DefaultListModel<>();
        playerList = new JList<>(playerListModel);
        JScrollPane playerScrollPane = new JScrollPane(playerList);

        // Кнопка для додавання нового гравця
        JButton addPlayerButton = new JButton("Add Player");
        addPlayerButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addPlayer();
            }
        });

        // Кнопка для зміни транспорту гравця
        JButton changeTransportButton = new JButton("Change Transport");
        changeTransportButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                changePlayerTransport();
            }
        });

        // Розміщення компонентів на вікні
        JPanel buttonPanel = new JPanel(new GridLayout(1, 2));
        buttonPanel.add(addPlayerButton);
        buttonPanel.add(changeTransportButton);

        getContentPane().setLayout(new BorderLayout());
        getContentPane().add(playerScrollPane, BorderLayout.CENTER);
        getContentPane().add(buttonPanel, BorderLayout.SOUTH);

        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                savePlayersToFile(playerListModel, "players.dat");
            }
        });

        loadPlayersFromFile("players.dat");
    }

    private Transport enterData(String selectedTransport) {
        if (selectedTransport != null) {
            switch (selectedTransport) {
                case "Car":
                    // Введення характеристик автомобіля
                    String carModel = JOptionPane.showInputDialog(this, "Enter Car Model:");
                    if (carModel == null || carModel.trim().isEmpty()) {
                        JOptionPane.showMessageDialog(this, "Car model cannot be empty.", "Add Player", JOptionPane.WARNING_MESSAGE);
                        return null;
                    }

                    String carYearStr = JOptionPane.showInputDialog(this, "Enter Car's Year:");
                    int carYear = Integer.parseInt(carYearStr);

                    String carSpeedStr = JOptionPane.showInputDialog(this, "Enter Car Speed:");
                    int carSpeed = Integer.parseInt(carSpeedStr);

                    String carCapacityStr = JOptionPane.showInputDialog(this, "Enter Car Capacity:");
                    int carCapacity = Integer.parseInt(carCapacityStr);

                    String carFuelType = JOptionPane.showInputDialog(this, "Enter Car Fuel Type:");

                    return new Car(carSpeed, carCapacity, carFuelType, carModel, carYear);
                case "Bus":
                    String busSeatsStr = JOptionPane.showInputDialog(this, "Enter Number of Bus Seats:");
                    int busSeats = Integer.parseInt(busSeatsStr);

                    String busSpeedStr = JOptionPane.showInputDialog(this, "Enter Bus Speed:");
                    int busSpeed = Integer.parseInt(busSpeedStr);

                    String busCapacityStr = JOptionPane.showInputDialog(this, "Enter Bus Capacity:");
                    int busCapacity = Integer.parseInt(busCapacityStr);

                    String busFuelType = JOptionPane.showInputDialog(this, "Enter Bus Fuel Type:");

                    return new Bus(busSpeed, busCapacity, busFuelType, busSeats);
                case "Motorcycle":
                    String motorcycleType = JOptionPane.showInputDialog(this, "Enter Motorcycle Type:");
                    if (motorcycleType == null || motorcycleType.trim().isEmpty()) {
                        JOptionPane.showMessageDialog(this, "Motorcycle type cannot be empty.", "Add Player", JOptionPane.WARNING_MESSAGE);
                        return null;
                    }

                    String motorcycleSpeedStr = JOptionPane.showInputDialog(this, "Enter Motorcycle Speed:");
                    int motorcycleSpeed = Integer.parseInt(motorcycleSpeedStr);

                    String motorcycleCapacityStr = JOptionPane.showInputDialog(this, "Enter Motorcycle Capacity:");
                    int motorcycleCapacity = Integer.parseInt(motorcycleCapacityStr);

                    String motorcycleFuelType = JOptionPane.showInputDialog(this, "Enter Motorcycle Fuel Type:");

                    return new Motorcycle(motorcycleSpeed, motorcycleCapacity, motorcycleFuelType, motorcycleType);
            }
        }
        return null;
    }

    private void addPlayer() {
        String playerName = JOptionPane.showInputDialog(this, "Enter Player Name:", "Add Player", JOptionPane.PLAIN_MESSAGE);
        if (playerName == null || playerName.trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "Player name cannot be empty.", "Add Player", JOptionPane.WARNING_MESSAGE);
            return;
        }

        String[] options = {"Car", "Bus", "Motorcycle"};
        String selectedTransport = (String) JOptionPane.showInputDialog(this, "Select Transport",
                "Add Player", JOptionPane.PLAIN_MESSAGE, null, options, options[0]);

        playerListModel.addElement(new Player(enterData(selectedTransport), playerName));
    }


    private void changePlayerTransport() {
        Player selectedPlayer = playerList.getSelectedValue();
        if (selectedPlayer == null) {
            JOptionPane.showMessageDialog(this, "Please select a player to change transport.",
                    "Change Transport", JOptionPane.WARNING_MESSAGE);
            return;
        }

        // Вибір нового типу транспортного засобу
        String[] options = {"Car", "Bus", "Motorcycle"};
        String selectedTransport = (String) JOptionPane.showInputDialog(this, "Select New Transport",
                "Change Transport", JOptionPane.PLAIN_MESSAGE, null, options, options[0]);

        selectedPlayer.setTransport(enterData(selectedTransport));
    }

    public static void savePlayersToFile(DefaultListModel<Player> playerListModel, String filename) {
        try (ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(filename))) {
            // Записуємо кількість гравців у файл
            outputStream.writeInt(playerListModel.size());

            // Записуємо кожного гравця та його транспортний засіб
            for (int i = 0; i < playerListModel.size(); i++) {
                Player player = playerListModel.getElementAt(i);
                outputStream.writeObject(player);
            }

            System.out.println("Players saved to file successfully.");
        } catch (IOException e) {
            System.out.println("Error saving players to file: " + e.getMessage());
        }
    }

    // Метод для завантаження гравців з файлу
    private void loadPlayersFromFile(String filename) {
        try (ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(filename))) {
            int numPlayers = inputStream.readInt();
            for (int i = 0; i < numPlayers; i++) {
                Player player = (Player) inputStream.readObject();
                playerListModel.addElement(player);
            }
            System.out.println("Players loaded from file successfully.");

            // Оновлюємо відображення списку гравців після завантаження
            playerList.revalidate();
            playerList.repaint();
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error loading players from file: " + e.getMessage());
        }
    }


    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Main().setVisible(true);
            }
        });
    }
}

