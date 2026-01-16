$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes  // Récupère tous les checkbox du tableau
	var checkbox = $('table tbody input[type="checkbox"]');

 // Gestion du bouton "Tout sélectionner"
	$("#selectAll").click(function(){
		if(this.checked){
            // Cocher tous les checkbox
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
            // Décocher tous les checkbox
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
     // Si on décoche un seul checkbox, décocher "Tout sélectionner"
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});