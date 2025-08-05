id0_JSON = {
"alias": "Freq ID 0",
"ignore_missing": False,
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "DAYS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    },
    "inclusive": False
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-effective-start-date"
    },
    "inclusive": True,
    "extend_from": "Friday",
    "extend_to": "Sunday"
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id1_JSON = {
"group-1": {
  "alias": "Freq ID 1 - Tuesday through Sunday",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "AGO",
      "skip_weekends": True
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "DAYS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date",
        "skip_weekends": True
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  },
  "rule_specific_days": [
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ]
},
"group-2": {
  "alias": "Freq ID 1 - Monday",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "AGO"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "DAYS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-effective-start-date"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  },
  "rule_specific_days": [
    "Monday"
  ]
}
}

id2_JSON = {
"alias": "Freq ID 2",
"ignore_missing": False,
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Friday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "DAYS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    },
    "inclusive": False
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-effective-start-date"
    },
    "inclusive": True,
    "extend_from": "Saturday",
    "extend_to": "Friday"
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id3_JSON = {
"alias": "Freq ID 3",
"ignore_missing": False,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 5,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Monday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "DAYS",
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "FOLLOWING",
    "weekday": "Friday"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 7,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id4_JSON = id3_JSON

id5_JSON = {
"alias": "Freq ID 5",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "SECOND",
    "direction": "PRECEDING",
    "weekday": "Sunday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS",
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "FOLLOWING",
    "weekday": "Saturday"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Saturday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id6_JSON = id5_JSON

id7_JSON = {
"alias": "Freq ID 7",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "MONTHS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "SECOND",
    "direction": "PRECEDING",
    "weekday": "Friday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS",
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "FOLLOWING",
    "weekday": "Thursday"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Thursday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
},
}

id8_JSON = id7_JSON

id13_JSON = {
  "alias": "Freq ID 13",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id14_JSON = id13_JSON

id15_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 2,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id16_JSON = id15_JSON

id17_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 3,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id18_JSON = id17_JSON

id19_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 4,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id20_JSON = id19_JSON

id21_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 5,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id22_JSON = id21_JSON

id23_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 6,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id24_JSON = id23_JSON

id25_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 7,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id26_JSON = id25_JSON

id27_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 8,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id28_JSON = id27_JSON

id29_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 9,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id30_JSON = id29_JSON

id31_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 10,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id32_JSON = id31_JSON

id33_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 11,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id34_JSON = id33_JSON

id35_JSON = {
"alias": "Freq ID 14",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 12,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id36_JSON = id35_JSON

id37_JSON = {
"alias": "CONTRACT_RULE_Q2_AVG",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "WEEKS",
    "direction": "AGO"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 6,
  "unit": "DAYS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id38_JSON = id37_JSON

id39_JSON = {
"alias": "CONTRACT_RULE_Q2_AVG",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 2,
    "unit": "WEEKS",
    "direction": "AGO"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 13,
  "unit": "DAYS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id40_JSON = id39_JSON

id41_JSON = {
"alias": "CONTRACT_RULE_Q2_AVG",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 3,
    "unit": "WEEKS",
    "direction": "AGO"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 20,
  "unit": "DAYS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id42_JSON = id41_JSON

id43_JSON = {
"alias": "CONTRACT_RULE_Q2_AVG",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 4,
    "unit": "WEEKS",
    "direction": "AGO"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 27,
  "unit": "DAYS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id44_JSON = id43_JSON

id45_JSON = {
"alias": "Freq ID 45",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "after-end-date",
      "snap_to": "beginning",
      "skip_weekends": True
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "QUARTERS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id46_JSON = id45_JSON

id47_JSON = {
"alias": "Freq ID 45",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 2,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "after-end-date",
      "snap_to": "beginning",
      "skip_weekends": True
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "QUARTERS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id48_JSON = id47_JSON

id49_JSON = {
"alias": "Freq ID 45",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 3,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "after-end-date",
      "snap_to": "beginning",
      "skip_weekends": True
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "QUARTERS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id50_JSON = id49_JSON

id51_JSON = {
"alias": "Freq ID 45",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 4,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "QUARTERS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "after-end-date",
      "snap_to": "beginning",
      "skip_weekends": True
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "QUARTERS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id52_JSON = id51_JSON

id53_JSON = {
"alias": "ID Freq 53",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Monday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Monday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id54_JSON = {
"alias": "ID Freq 54",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Tuesday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Tuesday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id55_JSON = {
"alias": "ID Freq 55",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Wednesday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Wednesday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}


id56_JSON = {
"alias": "ID Freq 56",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Thursday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Thursday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id9_JSON = {
"alias": "ID Freq 9",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Saturday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Saturday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id10_JSON = {
"alias": "ID Freq 10",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Sunday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Sunday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id57_JSON = {
"alias": "ID Freq 57",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Monday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Sunday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id58_JSON = {
"alias": "ID Freq 57",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Tuesday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Monday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id59_JSON = {
"alias": "ID Freq 57",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Wednesday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Tuesday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id60_JSON = {
"alias": "ID Freq 57",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Thursday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Wednesday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id61_JSON = {
"alias": "ID Freq 57",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Friday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Thursday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id62_JSON = {
"alias": "ID Freq 57",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 4,
    "unit": "DAYS",
    "direction": "AGO"
  },
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "PRECEDING",
    "weekday": "Monday"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS",
  "refine-by-weekday": {
    "position": "FIRST",
    "direction": "FOLLOWING",
    "weekday": "Friday"
  }
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "DAYS",
      "direction": "after-end-date"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Thursday"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id63_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id64_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 2,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id65_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 3,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id66_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 4,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id67_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 5,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 5,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id68_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 6,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 6,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id69_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 0,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "beginning"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id70_JSON = {
"alias": "Freq ID 63",
"ignore_missing": True,
"global-relative-from-today": "today",
"start_date": {
  "type": "relative",
  "relative-minor": {
    "value": 1,
    "unit": "MONTHS",
    "direction": "AGO",
    "snap_to": "end"
  }
},
"end_date": {
  "type": "relative_to_start",
  "value": 0,
  "unit": "MONTHS"
},
"day_filter": [
  {
    "type": "inclusive_days_of_week",
    "days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ]
  }
],
"aggregate": {
  "type": "MEAN",
  "by": "Volume",
  "first_day_only": True
},
"effective": {
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "after-end-date",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "after-effective-start-date",
      "snap_to": "end"
    }
  }
},
"repeat": {
  "interval": 2,
  "unit": "WEEK",
  "anchor_day": "Monday",
  "start": {
    "type": "absolute",
    "value": "2023-06-25"
  }
}
}

id71_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 2,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id72_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 3,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id73_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 4,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id74_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 5,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 5,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
} 

id75_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 6,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 6,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id76_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 0,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id77_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 2,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id78_JSON = id77_JSON

id79_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 2,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id81_JSON = {
  "alias": "Freq ID 63",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id82_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "QUARTERS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id83_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 5,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 3,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id84_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "MONTHS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id85_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "QUARTERS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id86_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 2,
        "unit": "QUARTERS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id87_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 3,
        "unit": "QUARTERS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id88_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 4,
        "unit": "QUARTERS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}


id89_JSON = {
  "alias": "Freq ID 82",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 6,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 2,
        "unit": "QUARTERS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id90_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 8,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "DAYS"
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id91_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 8,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 6,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
} #GOOD EXAMPLE: previous 3 months from 5 months ago [start, end]. From toay, start of month to end of current quarter [effective start, effective end]

id92_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 11,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 9,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id93_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id94_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id95_JSON = {
  "alias": "Freq ID 90",
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id96_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 4,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id97_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 7,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 5,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

{
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 5,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id98_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 5,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 3,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    },
    {
      "type": "days_between",
      "lower_bound": 1,
      "upper_bound": "1"
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id99_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MODE",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id100_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "WEEKS",
      "direction": "AGO"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "PRECEDING",
      "weekday": "Thursday"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS",
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Wednesday"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Simple",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      },
      "refine-by-weekday": {
        "position": "FIRST",
        "direction": "FOLLOWING",
        "weekday": "Wednesday"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id101_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "WEEKS",
      "direction": "AGO"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "PRECEDING",
      "weekday": "Thursday"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 0,
    "unit": "MONTHS",
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Wednesday"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "volume weighted",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      },
      "refine-by-weekday": {
        "position": "FIRST",
        "direction": "FOLLOWING",
        "weekday": "Wednesday"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

# id102_JSON = {
#   "alias": "Freq ID 90",
#   "ignore_missing": True,
#   "global-relative-from-today": "today",
#   "start_date": {
#     "type": "relative",
#     "relative-minor": {
#       "value": 1,
#       "unit": "QUARTERS",
#       "direction": "AGO",
#       "snap_to": "beginning"
#     }
#   },
#   "end_date": {
#     "type": "relative",
#     "relative-minor": {
#       "value": 1,
#       "unit": "QUARTERS",
#       "direction": "AGO",
#       "snap_to": "end"
#     }
#   },
#   "day_filter": [
#     {
#       "type": "inclusive_days_of_week",
#       "days": [
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#         "Sunday"
#       ]
#     },
#     {
#       "type": "days_between",
#       "lower_bound": 1,
#       "upper_bound": "1"
#     }
#   ],
#   "aggregate": {
#     "type": "MEAN",
#     "by": "",
#     "first_day_only": True
#   },
#   "effective": {
#     "start_date": {
#       "type": "relative",
#       "relative-minor": {
#         "value": 0,
#         "unit": "QUARTERS",
#         "direction": "before-global-relative-date",
#         "snap_to": "beginning"
#       }
#     },
#     "end_date": {
#       "type": "relative",
#       "relative-minor": {
#         "value": 0,
#         "unit": "QUARTERS",
#         "direction": "after-effective-start-date",
#         "snap_to": "end"
#       }
#     }
#   },
#   "repeat": {
#     "interval": 2,
#     "unit": "WEEK",
#     "anchor_day": "Monday",
#     "start": {
#       "type": "absolute",
#       "value": "2023-06-25"
#     }
#   }
# }

# id104_JSON = {
#   "alias": "Freq ID 90",
#   "ignore_missing": True,
#   "global-relative-from-today": "today",
#   "start_date": {
#     "type": "relative",
#     "relative-minor": {
#       "value": 0,
#       "unit": "MONTHS",
#       "direction": "AGO",
#       "snap_to": "beginning"
#     }
#   },
#   "end_date": {
#     "type": "relative",
#     "relative-minor": {
#       "value": 2,
#       "unit": "WEEKS",
#       "direction": "FROM NOW",
#       "snap_to": "beginning"
#     }
#   },
#   "day_filter": [
#     {
#       "type": "inclusive_days_of_week",
#       "days": [
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#         "Sunday"
#       ]
#     }
#   ],
#   "aggregate": {
#     "type": "MEAN",
#     "by": "",
#     "first_day_only": True
#   },
#   "effective": {
#     "start_date": {
#       "type": "relative",
#       "relative-minor": {
#         "value": 0,
#         "unit": "DAYS",
#         "direction": "before-global-relative-date"
#       }
#     },
#     "end_date": {
#       "type": "relative",
#       "relative-minor": {
#         "value": 0,
#         "unit": "QUARTERS",
#         "direction": "after-effective-start-date",
#         "snap_to": "end"
#       }
#     }
#   },
#   "repeat": {
#     "interval": 2,
#     "unit": "WEEK",
#     "anchor_day": "Monday",
#     "start": {
#       "type": "absolute",
#       "value": "2023-06-25"
#     }
#   }
# }

id105_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Friday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "before-global-relative-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id106_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "end"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Friday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "MONTHS",
        "direction": "after-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id107_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "MONTHS",
      "direction": "AGO",
      "snap_to": "beginning"
    },
    "refine-by-weekday": {
      "position": "THIRD",
      "direction": "FOLLOWING",
      "weekday": "Friday"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Friday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "MONTHS",
        "direction": "after-effective-start-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id108_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 29,
      "unit": "DAYS",
      "direction": "AGO",
      "snap_to": "beginning"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Monday"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 1,
    "unit": "DAYS",
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Monday"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-global-relative-date",
        "snap_to": "end"
      },
      "refine-by-weekday": {
        "position": "SECOND",
        "direction": "FOLLOWING",
        "weekday": "Monday"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id109_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 29,
      "unit": "DAYS",
      "direction": "AGO",
      "snap_to": "beginning"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Friday"
    }
  },
  "end_date": {
    "type": "relative_to_start",
    "value": 1,
    "unit": "DAYS",
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Friday"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Friday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-global-relative-date",
        "snap_to": "end"
      },
      "refine-by-weekday": {
        "position": "SECOND",
        "direction": "FOLLOWING",
        "weekday": "Monday"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

id110_JSON = {
  "alias": "Freq ID 90",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 29,
      "unit": "DAYS",
      "direction": "AGO",
      "snap_to": "beginning"
    },
    "refine-by-weekday": {
      "position": "FIRST",
      "direction": "FOLLOWING",
      "weekday": "Monday"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 29,
      "unit": "DAYS",
      "direction": "AGO"
    },
    "refine-by-weekday": {
      "position": "SECOND",
      "direction": "FOLLOWING",
      "weekday": "Friday"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Friday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-global-relative-date",
        "snap_to": "beginning"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "DAYS",
        "direction": "after-global-relative-date",
        "snap_to": "end"
      },
      "refine-by-weekday": {
        "position": "SECOND",
        "direction": "FOLLOWING",
        "weekday": "Monday"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

#this one frankly doesn't make sense: 
#description: "Average of 2 Weeks 1 Week Ago - Effective for 2 Weeks - Use For HORMEL"
#NOT 1 week ago though???
#and yet, start/end dates are [2 weeks from today, 1 day ago from today]
#effective is [1 week from today, 3 weeks after today]
id111_JSON = {
  "alias": "CONTRACT_RULE_Q2_AVG",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 2,
      "unit": "WEEKS",
      "direction": "AGO"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "DAYS",
      "direction": "AGO"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "WEEKS",
        "direction": "after-global-relative-date"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 13,
        "unit": "DAYS",
        "direction": "after-effective-start-date"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

#inteplast
id112_JSON = {
  "alias": "CONTRACT_RULE_Q2_AVG",
  "ignore_missing": True,
  "global-relative-from-today": "today",
  "start_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "beginning",
      "quarter_modifier":"inteplast"
    }
  },
  "end_date": {
    "type": "relative",
    "relative-minor": {
      "value": 1,
      "unit": "QUARTERS",
      "direction": "AGO",
      "snap_to": "end",
      "quarter_modifier":"inteplast"
    },
    "refine-by-days": {
      "value": 0,
      "direction": "PRECEDING"
    }
  },
  "day_filter": [
    {
      "type": "inclusive_days_of_week",
      "days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      ]
    }
  ],
  "aggregate": {
    "type": "MEAN",
    "by": "Volume",
    "first_day_only": True
  },
  "effective": {
    "start_date": {
      "type": "relative",
      "relative-minor": {
        "value": 1,
        "unit": "DAYS",
        "direction": "after-end-date"
      }
    },
    "end_date": {
      "type": "relative",
      "relative-minor": {
        "value": 0,
        "unit": "QUARTERS",
        "direction": "before-end-date",
        "snap_to": "end"
      }
    }
  },
  "repeat": {
    "interval": 2,
    "unit": "WEEK",
    "anchor_day": "Monday",
    "start": {
      "type": "absolute",
      "value": "2023-06-25"
    }
  }
}

ported_IDs = [[id0_JSON,0], [id1_JSON,1], [id2_JSON,2], [id3_JSON,3], [id4_JSON, 4], [id5_JSON, 5], [id6_JSON, 6], [id7_JSON, 7], [id8_JSON, 8], [id13_JSON, 13],
            [id14_JSON,14], [id15_JSON,15], [id16_JSON, 16], [id17_JSON,17], [id18_JSON, 18], [id19_JSON, 19], [id20_JSON,20], [id21_JSON, 21], [id22_JSON, 22],
            [id23_JSON, 23],[id24_JSON,24], [id25_JSON, 25], [id26_JSON,26], 
            [id27_JSON, 27], [id28_JSON, 28], [id29_JSON, 29], [id30_JSON, 30], [id31_JSON,31], [id32_JSON,32], [id33_JSON,33], [id34_JSON,34], [id35_JSON,35], [id36_JSON,36], [id37_JSON,37], [id38_JSON, 38], [id39_JSON,39], [id40_JSON,40], [id41_JSON,41], [id42_JSON,42], [id43_JSON,43],[id44_JSON,44], [id45_JSON,45], [id46_JSON,46],[id47_JSON,47],[id48_JSON,48],[id49_JSON,49],[id50_JSON,50],[id51_JSON,51],[id52_JSON,52],[id53_JSON,53], [id54_JSON,54], [id55_JSON,55], [id56_JSON,56], [id9_JSON, 9], [id10_JSON, 10], [id57_JSON,57], [id58_JSON,58], [id59_JSON,59], [id60_JSON,60], [id61_JSON,61], [id62_JSON,62], [id63_JSON,63], [id64_JSON,64], [id65_JSON,65], [id66_JSON,66], [id67_JSON,67],[id68_JSON,68],[id69_JSON,69], [id70_JSON,70], [id71_JSON,71], [id72_JSON,72], [id73_JSON,73], [id74_JSON,74], [id75_JSON,75],[id76_JSON,76], [id77_JSON,77],[id78_JSON,78],[id79_JSON,79],[id81_JSON,81], [id82_JSON,82],[id83_JSON,83],[id84_JSON,84],[id85_JSON,85],[id86_JSON,86],[id87_JSON,87], [id88_JSON,88], [id89_JSON,89],[id90_JSON,90], [id91_JSON,91], [id92_JSON,92], [id93_JSON,93],[id94_JSON,94], [id95_JSON,95], [id96_JSON,96],[id97_JSON,97],[id98_JSON,98], [id99_JSON,99], [id100_JSON,100], [id101_JSON,101],[id105_JSON,105], [id106_JSON,106], [id107_JSON,107], [id108_JSON,108], [id109_JSON,109], [id110_JSON,110],[id111_JSON,111]]

#ported_IDs = [[id112_JSON,112]]

#I want to add functionality to the special rule groupings.
