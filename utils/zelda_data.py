def parse_zelda_data(root):
    # Create a dictionary to store game segments and their entries
    game_segments = {}

    # Iterate through each 'gameSegment' element
    for segment in root.findall('.//gameSegment'):
        segment_header = segment.find('heading').text.strip() if segment.find('heading') is not None else None
        segment_id = segment.get('id')
        entries = []

        # Iterate through each 'entry' within the current game segment
        for entry in segment.findall('.//entry'):
            # Strip subheader and check for empty text
            subheader = entry.text.strip() if entry.text is not None else None
            if subheader == '':
                subheader = None # Set out subheader to none if text is empty

            entry_data = {
                'id': entry.get('id') if entry.get('id') is not None else None,
                'itemRef': entry.get('itemRef') if entry.get('itemRef') is not None else None,
                'checkbox': entry.get('checkbox') if entry.get('checkbox') is not None else None,
                'filters': entry.get('filters') if entry.get('filters') is not None else None,
                'type': entry.get('type') if entry.get('type') is not None else None,
                'subheader': subheader,
                'description': entry.find('description').text if entry.find('description') is not None else None,
                'name': entry.find('name').text if entry.find('name') is not None else None
            }
            entries.append(entry_data)

        # Store the entries in the game_segments dictionary
        game_segments[segment_id] = {
            'header': segment_header,
            'entries': entries
        }

    return game_segments
