<script>

let tu = window.location.href;
let ct = [];
let si = '#ID_OF_SELECT' 
			
			
$('#essai-trial option').each(function(i,v){
	
	k = '?page=';
	r = v.value;
	v = v.value.toLowerCase().replace(' ','-');
    v = v.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
	u = k + v;	
	                 
    ct.push({
		'r' : r,
		'v' : v,
		'u' : u,
	});
	
});

$.each(ct , function(i,v){
				
	if(tu.indexOf(v.v) > -1){
		$('' + si + ' [value ="'+ v.r + '"]').attr('selected' , 'selected'); 
	}
				
});

console.log(ct);

let urlTable = [];
let keyTable = [];

$.each(ct , function(i,v){	

	urlTable.push(v.u);		
	
});

$.each(ct , function(i,v){	

	keyTable.push(v.v);	
	
});

console.log(urlTable);
console.log(keyTable);

</script>