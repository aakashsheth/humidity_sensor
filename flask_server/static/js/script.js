$(function(){

	var onlineStatus = $("#header_status");
	var onButton = $("#turn_on");
	var offButton = $("#turn_off");
	var setButton = $('#set_button');
	var humidityAmount = $('#humidity_amount');

	var intervalId = setInterval(function(){
		getData();	  
	}, 1000);
	
	// Get the data the firs time the server runs
	getData();
	
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
        /*	{
              fillColor: "rgba(220,220,220,0.2)",
              strokeColor: "rgba(220,220,220,1)",
              pointColor: "rgba(220,220,220,1)",
              pointStrokeColor: "#fff",
              data: [65, 59, 80, 81, 56, 55, 40]
          	}
       */ ]
    },
    latestLabel = startingData.labels[6];

	// Reduce the animation steps for demo clarity.
	var myLiveChart = new Chart(ctx).Line(startingData, {animationSteps: 15});


	function getData(){
		$.ajax({
			url: "/all_settings",
			success: function(result){
				console.log(result);
				
				// Add two random numbers for each dataset
				//myLiveChart.addData([result['current_humidity']], ++latestLabel);
				// Remove the first point so we dont just add values forever
				//myLiveChart.removeData();

				// Update the UI
				//$('#current_setting').html(result['current_humidity_setting']);
				//$('#current_humidity_reading').html(result['current_humidity']);
				if(result['current_state'] == 'on')
				{
					onlineStatus.css('color', '#2ecc71');
					onlineStatus.html('Connected');
					onButton.hide()
					offButton.show()

					// Add two random numbers for each dataset
					myLiveChart.addData([result['current_humidity']], ++latestLabel);
					// Remove the first point so we dont just add values forever
					myLiveChart.removeData();

					// Update the UI
					$('#current_setting').html(result['current_humidity_setting']);
					$('#current_humidity_reading').html(result['current_humidity']);
				}
				else {
					onlineStatus.css('color', 'red');
					onlineStatus.html('Disconnected');
					onButton.show()
					offButton.hide()
				}

				$('#localIP').html(result['current_ip']);
			}
		})
	}

	onButton.on('click', function(){
		// Send AJAX ON request
		$.ajax({
			url: "/user_state/on",
			success: function(result){
				console.log('Turning on');
				console.log(result);
				onButton.hide();
				offButton.show();
				intervalId = setInterval(function(){
					getData();
				}, 1000);
			}
		})
	});

	offButton.on('click', function(){
		// Send AJAX OFF request
		clearInterval(intervalId);
		$.ajax({
			url: "/user_state/off",
			success: function(result){
				console.log(result);
				offButton.hide();
				onButton.show();
			}
		})
	});

	setButton.on('click', function(){
		
		// Set the humidity to the desired setting
		var url = "/change_humidity_setting/" + humidityAmount.val()
		
		$.ajax({
			url: url,
			success: function(result){
				console.log(result);
				console.log(url);
			}
		})
	});
})

