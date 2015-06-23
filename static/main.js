/*message='Are you sure you want to delete?';
result = window.confirm(message);

$('#deleteBtn').onclick(result);*/

$( document ).ready(function(){
	$('#tokyolink').on('mouseenter',
		function (){
			$('body').css('background','url("/img/tokyo.jpg")')
		}
	)
	$('#sflink').on('mouseenter',
		function (){
			$('body').css('background','url("/img/sf.jpg")')
		}
	)
	$('#londonlink').on('mouseenter',
		function (){
			$('body').css('background','url("/img/london.jpg")')
		}
	)}
)

