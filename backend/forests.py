FORESTS = [
    {
        'id': 1,
        'name': 'Anamalai Tiger Reserve',
        'location': {
            'district': 'Coimbatore',
            'latitude': 10.3750,
            'longitude': 77.0583,
            'elevation': 1400
        },
        'characteristics': {
            'area': 958,
            'vegetation': [
                {'type': 'Evergreen', 'percentage': 40, 'fire_risk_factor': 0.6},
                {'type': 'Semi-evergreen', 'percentage': 35, 'fire_risk_factor': 0.8},
                {'type': 'Moist deciduous', 'percentage': 25, 'fire_risk_factor': 1.2}
            ],
            'avg_biomass': 350
        },
        'media': {
            'image': 'anamalai.jpg',
            'map': 'anamalai_map.png'
        }
    },
    {
        'id': 2,
        'name': 'Mudumalai Tiger Reserve',
        'location': {
            'district': 'Nilgiris',
            'latitude': 11.5616,
            'longitude': 76.6469,
            'elevation': 1000
        },
        'characteristics': {
            'area': 321,
            'vegetation': [
                {'type': 'Dry deciduous', 'percentage': 50, 'fire_risk_factor': 1.4},
                {'type': 'Moist deciduous', 'percentage': 30, 'fire_risk_factor': 1.2},
                {'type': 'Teak forest', 'percentage': 20, 'fire_risk_factor': 1.6}
            ],
            'avg_biomass': 280
        },
        'media': {
            'image': 'mudumalai.jpg',
            'map': 'mudumalai_map.png'
        }
    },
    {
        'id': 3,
        'name': 'Sathyamangalam Wildlife Sanctuary',
        'location': {
            'district': 'Erode',
            'latitude': 11.5580,
            'longitude': 77.2812,
            'elevation': 750
        },
        'characteristics': {
            'area': 1408,
            'vegetation': [
                {'type': 'Dry thorn', 'percentage': 45, 'fire_risk_factor': 1.8},
                {'type': 'Scrub jungle', 'percentage': 30, 'fire_risk_factor': 2.0},
                {'type': 'Dry deciduous', 'percentage': 25, 'fire_risk_factor': 1.5}
            ],
            'avg_biomass': 190
        },
        'media': {
            'image': 'sathyamangalam.jpg',
            'map': 'sathyamangalam_map.png'
        }
    },
    {
        'id': 4,
        'name': 'Kalakad Mundanthurai Tiger Reserve',
        'location': {
            'district': 'Tirunelveli',
            'latitude': 8.6089,
            'longitude': 77.3210,
            'elevation': 1200
        },
        'characteristics': {
            'area': 895,
            'vegetation': [
                {'type': 'Tropical evergreen', 'percentage': 60, 'fire_risk_factor': 0.5},
                {'type': 'Wet deciduous', 'percentage': 40, 'fire_risk_factor': 0.9}
            ],
            'avg_biomass': 400
        },
        'media': {
            'image': 'kalakad.jpg',
            'map': 'kalakad_map.png'
        }
    },
    {
        'id': 5,
        'name': 'Srivilliputhur Grizzled Squirrel Wildlife Sanctuary',
        'location': {
            'district': 'Virudhunagar',
            'latitude': 9.5186,
            'longitude': 77.6435,
            'elevation': 800
        },
        'characteristics': {
            'area': 485,
            'vegetation': [
                {'type': 'Mixed deciduous', 'percentage': 55, 'fire_risk_factor': 1.3},
                {'type': 'Tropical dry forest', 'percentage': 45, 'fire_risk_factor': 1.6}
            ],
            'avg_biomass': 220
        },
        'media': {
            'image': 'srivilliputhur.jpg',
            'map': 'srivilliputhur_map.png'
        }
    },
    {
        'id': 6,
        'name': 'Gulf of Mannar Marine National Park',
        'location': {
            'district': 'Ramanathapuram',
            'latitude': 9.1840,
            'longitude': 79.0586,
            'elevation': 5
        },
        'characteristics': {
            'area': 560,
            'vegetation': [
                {'type': 'Mangrove', 'percentage': 70, 'fire_risk_factor': 0.3},
                {'type': 'Coastal scrub', 'percentage': 30, 'fire_risk_factor': 0.9}
            ],
            'avg_biomass': 100
        },
        'media': {
            'image': 'gulf_mannar.jpg',
            'map': 'gulf_mannar_map.png'
        }
    },
    {
        'id': 7,
        'name': 'Meghamalai Wildlife Sanctuary',
        'location': {
            'district': 'Theni',
            'latitude': 9.7167,
            'longitude': 77.3333,
            'elevation': 1500
        },
        'characteristics': {
            'area': 635,
            'vegetation': [
                {'type': 'Evergreen', 'percentage': 45, 'fire_risk_factor': 0.7},
                {'type': 'Moist deciduous', 'percentage': 35, 'fire_risk_factor': 1.2},
                {'type': 'Plantation', 'percentage': 20, 'fire_risk_factor': 1.0}
            ],
            'avg_biomass': 320
        },
        'media': {
            'image': 'meghamalai.jpg',
            'map': 'meghamalai_map.png'
        }
    },
    {
        'id': 8,
        'name': 'Angeles National Forest',
        'location': {
            'region': 'California',
            'latitude': 34.3333,
            'longitude': -118.0000,
            'elevation': 2200
        },
        'characteristics': {
            'area': 2650,
            'vegetation': [
                {'type': 'Chaparral', 'percentage': 50, 'fire_risk_factor': 2.5},
                {'type': 'Pine forests', 'percentage': 30, 'fire_risk_factor': 1.8},
                {'type': 'Dry shrublands', 'percentage': 20, 'fire_risk_factor': 3.0}
            ],
            'avg_biomass': 280
        },
        'media': {
            'image': 'angeles.jpg',
            'map': 'angeles_map.png'
        }
    },

{
    'id': 9,
    'name': 'Sundarbans National Park',
    'location': {
        'state': 'West Bengal',
        'latitude': 21.9497,
        'longitude': 89.1833,
        'elevation': 7
    },
    'characteristics': {
        'area': 1330,
        'vegetation': [
            {'type': 'Mangroves', 'percentage': 100, 'fire_risk_factor': 0.3}
        ],
        'avg_biomass': 180
    },
    'media': {
        'image': 'sundarbans.jpg',
        'map': 'sundarbans_map.png'
    }
},
{
    'id': 10,
    'name': 'Jim Corbett National Park',
    'location': {
        'state': 'Uttarakhand',
        'latitude': 29.5300,
        'longitude': 78.7747,
        'elevation': 1280
    },
    'characteristics': {
        'area': 520,
        'vegetation': [
            {'type': 'Sal forest', 'percentage': 70, 'fire_risk_factor': 1.1},
            {'type': 'Mixed deciduous', 'percentage': 30, 'fire_risk_factor': 1.4}
        ],
        'avg_biomass': 330
    },
    'media': {
        'image': 'corbett.jpg',
        'map': 'corbett_map.png'
    }
},
{
    'id': 11,
    'name': 'Amazon Rainforest',
    'location': {
        'region': 'Brazil',
        'latitude': -3.4653,
        'longitude': -62.2159,
        'elevation': 100
    },
    'characteristics': {
        'area': 5500000,
        'vegetation': [
            {'type': 'Rainforest', 'percentage': 100, 'fire_risk_factor': 0.9}
        ],
        'avg_biomass': 500
    },
    'media': {
        'image': 'amazon.jpg',
        'map': 'amazon_map.png'
    }
},
{
    'id': 12,
    'name': 'Australian Bushland',
    'location': {
        'region': 'New South Wales',
        'latitude': -33.8688,
        'longitude': 151.2093,
        'elevation': 300
    },
    'characteristics': {
        'area': 500000,
        'vegetation': [
            {'type': 'Eucalyptus', 'percentage': 70, 'fire_risk_factor': 2.0},
            {'type': 'Dry grasslands', 'percentage': 30, 'fire_risk_factor': 2.8}
        ],
        'avg_biomass': 240
    },
    'media': {
        'image': 'bushland.jpg',
        'map': 'bushland_map.png'
    }
}



]