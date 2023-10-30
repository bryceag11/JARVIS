p1=[-240,200];
p2=[240,200];
p3=[0,0];

for (deg=[90:1:90+16]){
    x1=cos(deg)*300;
    y1=sin(deg)*300;

    p4=[x1,y1];

    m=p4[1]/p4[0];

    ix=200/m;
    i=[ix,200];

    color("red")translate(i)cube([2,2,2],true);

    hull(){
        translate(p1)cube(1,true);
        translate(p2)cube(1,true);
    }
    hull(){
        translate(p3)cube(1,true);
        translate(p4)cube(1,true);
    }

}

//Ray
l=rands(200,10000,1)[0];
deg=rands(-16,16,1)[0];

color("red")rotate([deg,0,0])translate([-50,l/2,0])cube([2,l,2],true);
zr=sin(deg)*l;
yr=cos(deg)*l;
rep = [-50,yr,zr]; //rayendpoint
color("blue")translate(rep)cube(10,true);
rpp = [-50,yr,0]; //rayprojpoint
rppdeg=atan2( rpp[1],rpp[0]);
color("orange")translate(rpp)cube(10,true);
color("green")translate([-50,0,0])cube([2,yr,2]);

color("blue")hull(){
    translate(p3)cube(2,true);
    translate(rpp)cube(2,true);
}

mrpp=rpp[1]/rpp[0];
ix2=200/mrpp;
ipp=[ix2,200];
color("pink")translate(ipp)cube([1,1,320/4.19]);

//da rifare
mzpp=yr/zr;

iz=200/mzpp; //200??
izpp=[-480/4.19/2 , 200, iz];
color("aqua")translate(izpp)cube([480/4.19,1,1]);

//result
color("blue")translate([ix2,200,iz])cube([4,4,4],true);

//image
color("white",0.2)translate([0,200,0])cube([480,1,640]/4.19,true);
