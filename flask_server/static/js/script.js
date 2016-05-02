$(function(){


	var onlineStatus = $("#header_status");
	var onButton = $("#turn_on");
	var offButton = $("#turn_off");
	var setButton = $('#set_button');
	var humidityAmount = $('#humidity_amount');

	onButton.hide()
	offButton.hide()

	var canvas = document.getElementById('myChart'),
    ctx = canvas.getContext('2d'),
    startingData = {
      labels: [1, 2, 3, 4, 5, 6, 7],
      datasets: [
      		{
				fillColor: "rgba(220,220,220,0.2)",
				strokeColor: "rgba(220,220,220,1)",
				pointColor: "rgba(220,220,220,1)",
				pointStrokeColor: "#fff",
				data: [65, 59, 80, 81, 56, 55, 40]
			},
        	{
              fillColor: "rgba(220,220,220,0.2)",
              strokeColor: "rgba(220,220,220,1)",
              pointColor: "rgba(220,220,220,1)",
              pointStrokeColor: "#fff",
              data: [65, 59, 80, 81, 56, 55, 40]
          	}
        ]
    },
    latestLabel = startingData.labels[6];

	// Reduce the animation steps for demo clarity.
	var myLiveChart = new Chart(ctx).Line(startingData, {animationSteps: 15});


	setInterval(function(){
		getData();	  
	}, 1500);

	function getData(){
		$.ajax({
			url: "/data",
			success: function(result){
				console.log(result);
				
				// Add two random numbers for each dataset
				myLiveChart.addData([result['current_humidity'],result['current_temp']], ++latestLabel);
				// Remove the first point so we dont just add values forever
				myLiveChart.removeData();

				// Update the UI
				$('#current_setting').html(result['current_setting']);
				
				if(result['current_status'] === 'ON')
				{
					onlineStatus.css('color', 'green');
					onButton.hide()
					offButton.show()
				}
				else {
					onlineStatus.css('color', 'red');
					onButton.show()
					offButton.hide()
				}

				$('#localIP').html(result['ip']);
			}
		})
	}

	onButton.on('click', function(){
		// Send AJAX ON request
		alert("ON Button clicked");

		$.ajax({
			url: "/user_state/on",
			success: function(result){
				console.log(result);
			}
		})
	});

	offButton.on('click', function(){
		// Send AJAX OFF request
		alert("OFF Button clicked");

		$.ajax({
			url: "/user_state/off",
			success: function(result){
				console.log(result);
			}
		})
	});

	setButton.on('click', function(){
		// Set the humidity to the desired setting
		var url = "/change_humidity_setting/" + humidity_amount.val()

		$.ajax({
			url: url
			success: function(result){
				console.log(result);
			}
		})
	});
})

