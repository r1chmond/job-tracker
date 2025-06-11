
const totalJobs = document.getElementById("stat-total-jobs")?.innerHTML ?? 0
const bookmarkedJobs = document.getElementById("stat-bookmarked-jobs")?.innerHTML?? 0
const appliedJobs = document.getElementById("stat-applied-jobs")?.innerHTML?? 0
const interviewingJobs = document.getElementById("stat-interviewing-jobs")?.innerHTML?? 0
const offerJobs= document.getElementById("stat-offer-jobs")?.innerHTML?? 0
const rejectedJobs = document.getElementById("stat-rejected-jobs")?.innerHTML?? 0

const COLORS = {
  grey: "#949494",
  yellow: "#e8e464",
  red: "#e86464",
  green: "#64e88b",
  blue: "#64bee8",
  purple: "#754ee2"
}

let barChart = ""
const generateTotalJobChart = ()=> {
    const labels = ['Bookmarked', 'Applied', 'Interviewing', 'Offer', 'Not Selected' ]

    const data = { 
      labels: labels,
      datasets: [
      {
      label: false,
      data: [bookmarkedJobs, appliedJobs, interviewingJobs, offerJobs, rejectedJobs],
      borderColor: "",
      backgroundColor: [COLORS.grey,COLORS.yellow, COLORS.blue, COLORS.green, COLORS.red],
      borderWidth: 2,
      borderRadius: 5,
      borderSkipped: false,
      }
    ]
    }

const ctx = document.getElementById("bar-chart")
    
const config = {
     type: 'bar',
 data: data,
 options: {
    responsive: true,
    plugins: {
      legend:{
        display: false
      },
      title: {
        display: true,
        text: 'Job Status Comparison'
      }
    },
    scale: {
      y:{
        min: 0,
        max: Number(totalJobs),
        ticks:{
          stepSize: 1 
        },
      }
    }
  }
 };

 if (barChart){
     barChart.destroy();
 }
 barChart = new Chart(ctx, config)
}


let bookmarkedPieChart = ""

export const generateBookmarkedJobChart = () => {
  const remainingJobs = totalJobs-bookmarkedJobs
  const data = {
    labels: ['Bookmarked Jobs', 'Remaining Jobs'],
    datasets: [{
      label: " ",
      data: [bookmarkedJobs, remainingJobs],
      backgroundColor:[
        COLORS.grey,
        COLORS.purple
      ],
      hoverOffset: 4
    }]
  }

  const config = {
    type: "doughnut",
    data: data
  }

  const ctx = document.getElementById("bookmarked-chart")

  if (bookmarkedPieChart) {
    bookmarkedPieChart.destroy()
  }

  bookmarkedPieChart = new Chart(ctx, config)
}


let appliedPieChart = ""

export const generateAppliedJobChart = () => {
  const remainingJobs = totalJobs-appliedJobs
  const data = {
    labels: ['Applied Jobs', 'Remaining Jobs'],
    datasets: [{
      label: " ",
      data: [appliedJobs, remainingJobs],
      backgroundColor:[
        COLORS.yellow,
        COLORS.purple
      ],
      hoverOffset: 4
    }]
  }

  const config = {
    type: "doughnut",
    data: data
  }

  const ctx = document.getElementById("applied-chart")

  if (appliedPieChart) {
    appliedPieChart.destroy()
  }

  appliedPieChart = new Chart(ctx, config)
}


let interviewingPieChart = ""

export const generateInterviewingJobChart = () => {
  const remainingJobs = totalJobs-interviewingJobs
  const data = {
    labels: ['Interviewing Jobs', 'Remaining Jobs'],
    datasets: [{
      label: " ",
      data: [interviewingJobs, remainingJobs],
      backgroundColor:[
        COLORS.blue,
        COLORS.purple
      ],
      hoverOffset: 4
    }]
  }

  const config = {
    type: "doughnut",
    data: data
  }

  const ctx = document.getElementById("interviewing-chart")

  if (interviewingPieChart) {
    interviewingPieChart.destroy()
  }

  interviewingPieChart = new Chart(ctx, config)
}


let offerPieChart = ""

export const generateOfferJobChart = () => {
  const remainingJobs = totalJobs-offerJobs
  const data = {
    labels: ['Offer Jobs', 'Remaining Jobs'],
    datasets: [{
      label: " ",
      data: [offerJobs, remainingJobs],
      backgroundColor:[
        COLORS.green,
        COLORS.purple
      ],
      hoverOffset: 4
    }]
  }

  const config = {
    type: "doughnut",
    data: data
  }

  const ctx = document.getElementById("offer-chart")

  if (offerPieChart) {
    offerPieChart.destroy()
  }

  offerPieChart = new Chart(ctx, config)
}

let rejectedPieChart = ""

export const generateRejectedJobChart = () => {
  const remainingJobs = totalJobs-rejectedJobs
  const data = {
    labels: ['Not Selected Jobs', 'Remaining Jobs'],
    datasets: [{
      label: " ",
      data: [rejectedJobs, remainingJobs],
      backgroundColor:[
        COLORS.red,
        COLORS.purple
      ],
      hoverOffset: 4
    }]
  }

  const config = {
    type: "doughnut",
    data: data
  }

  const ctx = document.getElementById("rejected-chart")

  if (rejectedPieChart) {
    rejectedPieChart.destroy()
  }

  rejectedPieChart = new Chart(ctx, config)
}

export const showChart = () =>{
  generateTotalJobChart()
  generateBookmarkedJobChart()
  generateAppliedJobChart()
  generateInterviewingJobChart()
  generateOfferJobChart()
  generateRejectedJobChart()
}
