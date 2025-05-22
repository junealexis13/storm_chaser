from enum import Enum


class Places(Enum):
    PLACES = {
    'Bataan': [
        'Abucay',
        'Bagac',
        'City of Balanga (Capital)',
        'Dinalupihan',
        'Limay',
        'Mariveles',
        'Morong',
        'Orani',
        'Orion',
        'Pilar',
        'Samal'
    ],
    'Bulacan': [
        'Bulakan',
        'Hagonoy',
        'Paombong',
        'Obando',
        'City of Malolos (Capital)'
    ],
    'Pampanga': [
        'Lubao',
        'Macabebe',
        'Masantol',
        'Sasmuan (Sexmoan)'
    ],
    'Aurora': [
        'Baler (Capital)',
        'Casiguran',
        'Dilasag',
        'Dinalungan',
        'Dipaculao',
        'Maria Aurora',  # partly inland but may have access via river
        'San Luis',
        'Dingalan'
    ],
    'Zambales': [
        'Botolan',
        'Cabangan',
        'Candelaria',
        'Iba (Capital)',
        'Masinloc',
        'Palauig',
        'San Antonio',
        'San Felipe',
        'San Marcelino',  # has access via Subic Bay
        'San Narciso',
        'Santa Cruz',
        'Subic',
        'Olongapo City'
    ]
}