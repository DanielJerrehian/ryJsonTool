# ryJsonTool
A simple tool to create JSON files used for the React player on raveyardsounds.com

## Example
Call the function `main` in `main.py` with the required parameters, specifically `directory`, `google_folder_name`, and `json_file_name`.
For other packs, the `tags` within `tags.py` need to be updated to match the folder structure of the sample pack.

```py
main(
  directory=os.path.join("Sample", "Pack", "Path"),
  google_folder_name="The path of the Google Storage URL",
  json_file_name="The desired name of the output JSON file"
)
```
