$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-element').modal('show');
			},
			success: function(data){
				$('#modal-element .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#element-table tbody').html(data.element_list);
					$('#modal-element').modal('hide');

				} else {
					$('#modal-element .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create
$("#element_form").click(ShowForm);
$("#modal-element").on("submit","#form",SaveForm);

//update
$('#element-table').on("click",".show-form-update",ShowForm);
$('#modal-element').on("submit",".update-form",SaveForm)

//delete
$('#element-table').on("click",".show-form-delete",ShowForm);
$('#modal-element').on("submit",".delete-form",SaveForm)
} );


$(document).ready(function(){
	var ShowForm3 = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-phase').modal('show');
			},
			success: function(data){
				$('#modal-phase .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm3 =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#phase-table tbody').html(data.element_list);
					$('#modal-phase').modal('hide');

				} else {
					$('#modal-phase .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create
$("#phase_form").click(ShowForm3);
$("#modal-phase").on("submit","#form",SaveForm3);

//update
$('#phase-table').on("click",".show-form-update",ShowForm3);
$('#modal-phase').on("submit",".update-form",SaveForm3)

//delete
$('#phase-table').on("click",".show-form-delete",ShowForm3);
$('#modal-phase').on("submit",".delete-form",SaveForm3)
} );

