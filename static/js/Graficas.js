new Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'myfirstchart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [
      { year: '2018', value: 50 },
      { year: '2019', value: 62 },
      { year: '2020', value: 69 },
      { year: '2021', value: 75 },
      { year: '2022', value: 99 }
    ],
    // The name of the data record attribute that contains x-values.
    xkey: 'year',
    // A list of names of data record attributes that contain y-values.
    ykeys: ['value'],
    // Labels for the ykeys -- will be displayed when you hover over the
    // chart.
    labels: ['Usuarios'],
    resize: true

  });

/*
 * Play with this code and it'll update in the panel opposite.
 *
 * Why not try some of the options above?
 */
Morris.Donut({
  element: 'graficoanillos',
  data: [
    {label: "Formarte", value: 4},
    {label: "Alimentarte", value: 30},
    {label: "Cuidarte", value: 22},
    {label: "Bienestar", value: 30},
    {label: "Impulsarte", value: 10}
  ]
});



