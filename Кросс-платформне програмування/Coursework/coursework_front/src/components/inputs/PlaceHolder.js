import React, { useState } from 'react';
import { FormControl, Select, MenuItem, OutlinedInput, Box } from '@mui/material';

const ITEM_HEIGHT = 28;
const ITEM_PADDING_TOP = 5.33;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
    },
  },
};

const filterOptions = [
  { value: 'default', label: 'Default' },
  { value: 'sortByDestination', label: 'By destination' },
  { value: 'sortByDepartureDate', label: 'By departure date' },
];

function ApplicationFilterSelect({ onSelectChange }) {
  const [selectedOption, setSelectedOption] = useState('default');

  const handleChange = (event) => {
    const { value } = event.target;
    setSelectedOption(value);
    onSelectChange(value);
  };

  return (
    <Box display="flex" alignItems="center" gap={2}>
      <FormControl sx={{ width: 200}}>
        <Select
          displayEmpty
          value={selectedOption}
          onChange={handleChange}
          input={<OutlinedInput />}
          renderValue={(selected) => {
            if (!selected || selected === 'default') {
              return <>Default</>;
            }

            const selectedOption = filterOptions.find(option => option.value === selected);
            return selectedOption ? selectedOption.label : <>Default</>;
          }}
          MenuProps={MenuProps}
          inputProps={{ 'aria-label': 'Without label' }}
        >
          {filterOptions.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}

export default ApplicationFilterSelect;
