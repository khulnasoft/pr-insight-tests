from pr_assistant.tools.pr_description import insert_br_after_x_chars

class TestBR:
    def test_br1(self):
        file_change_description = '- Imported `FilePatchInfo` and `EDIT_TYPE` from `pr_assistant.algo.types` instead of `pr_assistant.git_providers.git_provider`.'
        file_change_description_br = insert_br_after_x_chars(file_change_description)
        expected_output = generate_html_list_item('Imported', 'FilePatchInfo', 'EDIT_TYPE', 'pr_assistant.algo.types', 'pr_assistant.git_providers.git_provider')
        assert file_change_description_br == expected_output

    def test_br2(self):
        file_change_description = (
            '- Created a - new -class `ColorPaletteResourcesCollection ColorPaletteResourcesCollection '
            'ColorPaletteResourcesCollection ColorPaletteResourcesCollection`')
        file_change_description_br = insert_br_after_x_chars(file_change_description)
        expected_output = ('<li>Created a - new -class <code>ColorPaletteResourcesCollection </code><br><code>'
                           'ColorPaletteResourcesCollection ColorPaletteResourcesCollection '
                           '</code><br><code>ColorPaletteResourcesCollection</code>')
        assert file_change_description_br == expected_output

    def test_br3(self):
        file_change_description = 'Created a new class `ColorPaletteResourcesCollection` which extends `AvaloniaDictionary<ThemeVariant, ColorPaletteResources>` and implements aaa'
        file_change_description_br = insert_br_after_x_chars(file_change_description)
        expected_output = ('Created a new class <code>ColorPaletteResourcesCollection</code> which '
                           'extends <br><code>AvaloniaDictionary<ThemeVariant, ColorPaletteResources>'
                           '</code> and implements <br>aaa')
        assert file_change_description_br == expected_output
