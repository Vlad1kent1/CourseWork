package org.example.models;

import org.example.models.Transport;
import java.io.Serializable;

public class Player implements Serializable {
    private String name;
    private Transport transport;

    public Player(Transport transport, String name) {
        this.name = name;
        this.transport = transport;
    }

    public Transport getTransport() {
        return transport;
    }

    public void setTransport(Transport transport) {
        this.transport = transport;
    }

    public void changeTransport(Transport newTransport) {
        System.out.println("Changing Player's Transport...");
        transport = newTransport;
        System.out.println("Player's Transport changed successfully!");
    }

    @Override
    public String toString() {
        return name + "'s Transport: " + transport.displayInfo();
    }
}
