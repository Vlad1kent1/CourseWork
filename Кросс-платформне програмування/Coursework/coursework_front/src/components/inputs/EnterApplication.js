import React, { useState } from "react";
import { styled } from "@mui/material/styles";
import { Paper, Typography, Stack, TextField, Button } from "@mui/material";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider, DatePicker } from "@mui/x-date-pickers";
import Tooltip from "@mui/material/Tooltip";
import dayjs from "dayjs";
import {
  validateDestination,
  validateFlightNumber,
  validatePassengerName,
  validateDate,
} from "../services/Validations";

const ProSpan = styled("span")({
  display: "inline-block",
  height: "1em",
  width: "1em",
  verticalAlign: "middle",
  marginLeft: "0.3em",
  marginBottom: "0.08em",
  backgroundSize: "contain",
  backgroundRepeat: "no-repeat",
  backgroundImage: "url(https://mui.com/static/x/pro.svg)",
});

function Label({ componentName, valueType, isProOnly }) {
  const content = <span>{componentName}</span>;

  if (isProOnly) {
    return (
      <Stack direction="row" spacing={0.5} component="span">
        <Tooltip title="Included on Pro package">
          <a
            href="https://mui.com/x/introduction/licensing/#pro-plan"
            aria-label="Included on Pro package"
          >
            <ProSpan />
          </a>
        </Tooltip>
        {content}
      </Stack>
    );
  }

  return content;
}

export default function EnterDialog({
  isEditing,
  handleClose,
  initialData,
  handleSave,
}) {
  const [id] = useState(initialData ? initialData.id : "");
  const [destination, setDestination] = useState(
    initialData ? initialData.destination : ""
  );
  const [flightNumber, setFlightNumber] = useState(
    initialData ? initialData.flightNumber : ""
  );
  const [passengerName, setPassengerName] = useState(
    initialData ? initialData.passengerName : ""
  );
  const [departureDate, setDepartureDate] = useState(
    initialData && initialData.departureDate
      ? dayjs(initialData.departureDate)
      : null
  );
  const [errors, setErrors] = useState({});

  const handleClick = (e) => {
    e.preventDefault();
    const newErrors = {};

    if (!validateDestination(destination)) {
      newErrors.destination =
        "Destination must start with a capital letter and contain only letters and spaces.";
    }

    if (!validateFlightNumber(flightNumber)) {
      newErrors.flightNumber = 'Flight number must be in the format "AB 1234".';
    }

    if (!validatePassengerName(passengerName)) {
      newErrors.passengerName =
        'Passenger name must be in the format "Smith J.A.".';
    }

    if (!validateDate(departureDate)) {
      newErrors.departureDate = "Departure date must be in the future.";
    }

    if (Object.keys(newErrors).length === 0) {
      const formattedDepartureDate = departureDate
        ? departureDate.toDate()
        : null;
      const data = {
        id,
        destination,
        flightNumber,
        passengerName,
        departureDate: formattedDepartureDate,
      };
      console.log(data);
      handleSave(data);
      handleClose();
    } else {
      setErrors(newErrors);
    }
    e.preventDefault();
  };

  return (
    <Paper elevation={3} style={{ padding: "20px", overflow: "hidden" }}>
      <Typography variant="h3" align="center" color="primary">
        {isEditing ? "Edit Application" : "Add New Application"}
      </Typography>
      <Stack spacing={2}>
        <TextField
          label="Destination"
          variant="standard"
          value={destination}
          onChange={(e) => setDestination(e.target.value)}
          error={!!errors.destination}
          helperText={errors.destination}
        />
        <TextField
          label="Flight number"
          variant="standard"
          value={flightNumber}
          onChange={(e) => setFlightNumber(e.target.value)}
          error={!!errors.flightNumber}
          helperText={errors.flightNumber}
        />
        <TextField
          label="Passenger name"
          variant="standard"
          value={passengerName}
          onChange={(e) => setPassengerName(e.target.value)}
          error={!!errors.passengerName}
          helperText={errors.passengerName}
        />
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DatePicker
            label={<Label componentName="Departure date" valueType="date" />}
            value={departureDate}
            onChange={(date) => setDepartureDate(date)}
            minDate={dayjs()} // Ensures that all past dates are disabled
            renderInput={(params) => (
              <TextField
                {...params}
                error={!!errors.departureDate}
                helperText={errors.departureDate}
              />
            )}
          />
        </LocalizationProvider>
        <Button variant="contained" onClick={handleClick}>
          Submit
        </Button>
      </Stack>
    </Paper>
  );
}
