# fcards

This script will navigate through your [Obsidian](https://obsidian.md/) notes to collect marked word/sentences/pagraphs, adding them to a raw list (each marked passage as a bullet point) and finally exporting them to a `txt` file.

The script was first written with the idea of creating flash cards (thus fcards) with key passages from diverse notes.

### Marking/Selecting Content

- Use `{{fcards}}` and `{{/fcards}}`. Example:

```
This is a sample text with {{fcards}}important content{{/fcards}} that should be marked.
Another line with {{fcards}}another important segment{{/fcards}}.
```
- Output: a `txt` file with:

```
- important content
- another important segment.
```

### Set the Variables within the main function:

- `base_path` Obsidian's vault location.
- `vault_name` Obsidian's vault name.
- `selected_folder` Folder within the vault that contains the notes you want to process.
- `output_text_path` Where the final file will be exported to.

### Boom!

- Run `fcards.py`
