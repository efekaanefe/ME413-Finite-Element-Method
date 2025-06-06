L = 1.0;  // adjust length as needed

// Bottom layer (z = 0)
Point(1) = {0,    0,    0, 1.0}; // node 0
Point(2) = {0,    L,    0, 1.0}; // node 1
Point(3) = {L,    0,    0, 1.0}; // node 2
Point(4) = {L,    L,    0, 1.0}; // node 3
Point(5) = {2*L,  0,    0, 1.0}; // node 4

// Top layer (z = 1)
Point(6) = {0,    0,    1, 1.0}; // node 5
Point(7) = {0,    L,    1, 1.0}; // node 6
Point(8) = {L,    0,    1, 1.0}; // node 7
Point(9) = {L,    L,    1, 1.0}; // node 8
Point(10)= {2*L,  1,    0, 1.0}; // node 9

Line(1) = {1, 2};
Line(2) = {1, 3};
Line(3) = {3, 6};
Line(4) = {2, 4};
Line(5) = {3, 4};
Line(6) = {3, 5};

Line(7)  = {6, 7};
Line(8)  = {6, 8};
Line(9)  = {4, 7};
Line(10) = {7, 9};
Line(11) = {8, 9};
Line(12) = {9, 10};
Line(13) = {5, 10};

Line(14) = {1, 6};
Line(15) = {2, 7};
Line(16) = {3, 8};
Line(17) = {4, 9};
Line(18) = {5, 10};
Line(19) = {6,7};
Line(20) = {4, 10};
Line(21) = {5, 8};
Line(22) = {4, 5};
Line(23) = {3, 10};
Line(24) = {1, 8};
Line(25) = {2, 9};


// Define physical groups
Physical Line("TrussElements") = {1:26};
Physical Point("FixedNodes") = {1, 2, 6, 7}; 
Physical Point("LoadNodes")  = {5, 10}; 