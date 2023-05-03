$(document).ready(function() {
	// Attach event listeners to input and button
	$('#language_code').on('keypress', function(event) {
		if (event.which === 13) { // ENTER key
			getTranslation();
		}
	});

	$('#btn_translate').click(function() {
		getTranslation();
	});

	// Function to fetch translation and update HTML
	function getTranslation() {
		var languageCode = $('#language_code').val();
		var url = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;
		$.getJSON(url, function(data) {
			$('#hello').text(data.hello);
		}).fail(function(jqXHR, textStatus, errorThrown) {
			$('#hello').text('Error: ' + errorThrown);
		});
	}
});
