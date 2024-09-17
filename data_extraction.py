import rpa

def extract_data_from_table(table_locator, row_index, column_indexes):
  """
  Extracts data from a specific row and columns of a table.

  Args:
      table_locator: A selector string to identify the table element.
      row_index: The zero-based index of the row to extract data from.
      column_indexes: A list of zero-based indexes for desired columns.

  Returns:
      A list of extracted data values from the specified row and columns.
  """
  # Navigate to the table element
  rpa.wait_until_visible(table_locator)

  # Get all table rows
  rows = rpa.get_element_attribute(table_locator, "data-text").splitlines()

  # Extract data from the specified row and columns
  extracted_data = []
  if row_index < len(rows):
    row_data = rows[row_index].split()
    for col_index in column_indexes:
      if col_index < len(row_data):
        extracted_data.append(row_data[col_index])
      else:
        extracted_data.append("")  # Handle out-of-bounds column index

  return extracted_data

def main():
  """
  Example usage of extract_data_from_table function.
  """
  table_locator = "table[class='data-table']"  # Replace with specific locator
  row_index = 1  # Extract data from the second row
  column_indexes = [0, 2]  # Extract data from first and third columns

  extracted_data = extract_data_from_table(table_locator, row_index, column_indexes)
  print(f"Extracted data: {extracted_data}")

if __name__ == "__main__":
  main()
