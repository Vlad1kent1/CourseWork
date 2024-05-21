package com.example.Coursework_back.models;

import jakarta.persistence.*;
import jakarta.validation.constraints.Future;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;
import lombok.Data;
import org.springframework.format.annotation.DateTimeFormat;

import java.util.Date;

@Data
@Entity
@Table(name = "application")
public class Application {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "destination")
    @NotBlank(message = "Destination is required")
    @Pattern(regexp = "^[a-zA-Z ]+$", message = "Destination must contain only alphabets and spaces")
    private String destination;

    @Column(name = "flight_number")
    @NotBlank(message = "Flight number is required")
    @Pattern(regexp = "^[A-Z0-9 ]+$", message = "Flight number must contain only uppercase alphabets, numbers, and spaces")
    private String flightNumber;

    @Column(name = "passenger_name")
    @NotBlank(message = "Passenger name is required")
    @Pattern(regexp = "^[A-Z][a-zA-Z]+(\\s[A-Z][a-zA-Z.]+)*$", message = "Passenger name must start with an uppercase letter, followed by alphabets, spaces, and optional points. The first letter of each word must be uppercase.")
    private String passengerName;

    @Column(name = "departure_date")
    @DateTimeFormat(pattern = "yyyy-MM-dd")
    @Temporal(TemporalType.DATE)
    @Future
    @NotNull(message = "Departure date is required")
    private Date departureDate;
}
