import React, { useState } from 'react';
import { styled } from "@mui/material/styles";
import { TextField, Button, Box, Stack } from '@mui/material';
import { LocalizationProvider, DatePicker } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import Tooltip from "@mui/material/Tooltip";

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

export default function SearchByFlightAndDate ({onSearch}) {
  const [flightNumber, setFlightNumber] = useState('');
  const [departureDate, setDepartureDate] = useState(null);

  const handleClick = () => {
    onSearch({ flightNumber, departureDate });
    setFlightNumber('');
    setDepartureDate(null);
  };

  return (
    <Box display="flex" alignItems="center" gap={2}>
      <TextField
        label="Flight number"
        variant="standard"
        value={flightNumber}
        onChange={(e) => setFlightNumber(e.target.value)}
      />
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DatePicker
          label={<Label componentName="Departure date" valueType="date" />}
          value={departureDate}
          onChange={(date) => setDepartureDate(date)}
          renderInput={(params) => <TextField {...params} />}
        />
      </LocalizationProvider>
      <Button variant="contained" onClick={handleClick} style={{ height: "max" }}>
        Search
      </Button>
    </Box>
  );
};
