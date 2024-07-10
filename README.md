### Marking/Selecting Content

- Use `{{fcards}}` and `{{/fcards}}`. Example:

```
This is a sample text with {{fcards}}important content{{/fcards}} that should be marked.
Another line with {{fcards}}another important segment{{/fcards}}.
```

### Set the Variables within the main function:

- `base_path` Obsidian's vault location.
- `vault_name` Obsidian's vault name.
- `selected_folder` Folder within the vault that contains the notes you want to process.
- `output_text_path` Where the final file will be exported to.

### Boom!

- Run `fcards.py`
