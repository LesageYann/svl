Feature: calculate the optimal weight with the height 

    formula : taille x 100 - 100 - (taille x 100 - 150) / 4

    Scenario Outline: weight computations
    	Given values height in cm 
	Then with <centimeter> height I obtain a weight of <kg> weight

    Examples: temperature values
    	| centimeter | kg         |
 	| 100	     | 12.5       |
	| 150	     | 50         |
	| 200	     | 87.5       |
