
function divLoaded(){

    const pointArray = [];

    var i = 0;
    while (i < 28){
        pointArray.push([Math.random(), Math.random()])
        console.log(pointArray[i])
        i++
    }

    landingDIV = document.getElementById('landing-div');
    console.log(landingDIV)
    canvas = document.getElementById('landing-canvas');
    console.log(canvas)
    ctx = canvas.getContext('2d');
    console.log(ctx)



    landingDIV.addEventListener("mousemove", (event) =>{

        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        ctx.beginPath();

        ctx.arc(event.pageX, event.pageY - (1/9) * canvas.height, 5, 0, 2 * Math.PI);
        ctx.fillStyle = "Black";
        ctx.fill();

        ctx.stroke();
        i = 0;
        while (i < pointArray.length){
            var distance = Math.sqrt(Math.pow(Math.abs(event.pageX - pointArray[i][0] * canvas.width), 2) + Math.pow(Math.abs(event.pageY - pointArray[i][1] * canvas.height), 2))
            ctx.beginPath();
            ctx.arc(pointArray[i][0]*canvas.width,pointArray[i][1]*(canvas.height),1,0,2*Math.PI);
            ctx.stroke();
            if( distance < 255 ){
                ctx.strokeStyle = (`rgba(52, 68, 73, ${(255/distance) - 1})`);
                ctx.lineTo(event.pageX,event.pageY - canvas.height * (1/9));
            }
            ctx.stroke();
            ctx.strokeStyle = ('rgba(0,0,0,1')
            i++
        }
    });
};



function retrieve_project(fileName){
    console.log(fileName);
    $.ajax({
        method: "GET",
        url: "/get_project_file",
        data: {nameOfFile: fileName},
        success: function(data){
            $("#project-viewer-id").html(data.result)
        }
    })
}