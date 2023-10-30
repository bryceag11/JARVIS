module lidar(){
    $fn=160;
    rotate([-90,0,90])translate([0,0,-10]){
        color("black")translate([0,0,-8])linear_extrude(10)import("ylidar.dxf","base");
        color("black")translate([0,0,-15])linear_extrude(2)import("ylidar.dxf","base");
        color("gray")translate([0,0,-20])linear_extrude(20)import("ylidar.dxf","motor");
        color("blue")linear_extrude(20)import("ylidar.dxf","rotor1");
        color("blue")linear_extrude(4)import("ylidar.dxf","rotor2");
        color("red")translate([0,0,-20])linear_extrude(20)import("ylidar.dxf","legs");
    }
}

module lidar_support(){
    translate([0,44,0])rotate([0,sin($t*360)*45,0]){
        lidar();
        color("gray",0.5){
            translate([0,-40,0])cube([50,3,30],true);
            translate([26,-3.5,0])cube([3,76,30],true);    
        }
        color("black")translate([0,-42,0])rotate([90,0,0])cylinder(2,22.5,22.5,true);
    }
}

lidar_support();
