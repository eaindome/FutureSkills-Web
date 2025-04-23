<script lang="ts">
  import { onMount } from 'svelte';
  
  export let data: {
    currentJob: {
      name: string;
      data: { year: number; jobs: number }[];
    };
    recommendedJob: {
      name: string;
      data: { year: number; jobs: number }[];
    };
  };
  
  let chart: HTMLDivElement | null = null;
  
  onMount(() => {
    renderChart();
    
    // Handle window resize
    const handleResize = () => {
      if (chart) renderChart();
    };
    
    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  });
  
  function renderChart() {
    if (!chart) return;
    
    const chartWidth = chart.clientWidth;
    const svgWidth = Math.min(600, chartWidth);
    const svgHeight = 250;
    const margin = { top: 20, right: 20, bottom: 40, left: 50 };
    const width = svgWidth - margin.left - margin.right;
    const height = svgHeight - margin.top - margin.bottom;
    
    // Create SVG
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", svgWidth.toString());
    svg.setAttribute("height", svgHeight.toString());
    svg.setAttribute("viewBox", `0 0 ${svgWidth} ${svgHeight}`);
    svg.setAttribute("class", "job-trends-chart");
    
    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
    g.setAttribute("transform", `translate(${margin.left},${margin.top})`);
    svg.appendChild(g);
    
    // X scale
    const years = data.currentJob.data.map(d => d.year);
    const xScale = (year: number) => {
      const min = Math.min(...years);
      const max = Math.max(...years);
      return (year - min) / (max - min) * width;
    };
    
    // Y scale
    const allJobs = [
      ...data.currentJob.data.map(d => d.jobs),
      ...data.recommendedJob.data.map(d => d.jobs)
    ];
    const yMin = Math.min(...allJobs) * 0.9; // Add some padding
    const yMax = Math.max(...allJobs) * 1.1;
    const yScale = (jobs: number) => {
      return height - (jobs - yMin) / (yMax - yMin) * height;
    };
    
    // Add grid lines
    const gridLines = document.createElementNS("http://www.w3.org/2000/svg", "g");
    gridLines.setAttribute("class", "grid-lines");
    
    // Horizontal grid lines
    const yTicks = 5;
    Array.from({ length: yTicks }).forEach((_, i) => {
      const value = yMin + (yMax - yMin) * i / (yTicks - 1);
      const gridLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
      gridLine.setAttribute("x1", "0");
      gridLine.setAttribute("y1", yScale(value).toString());
      gridLine.setAttribute("x2", width.toString());
      gridLine.setAttribute("y2", yScale(value).toString());
      gridLine.setAttribute("stroke", "#E2E8F0");
      gridLine.setAttribute("stroke-width", "1");
      gridLines.appendChild(gridLine);
    });
    
    g.appendChild(gridLines);
    
    // X-axis label
    const xAxisLabel = document.createElementNS("http://www.w3.org/2000/svg", "text");
    xAxisLabel.setAttribute("x", (width / 2).toString());
    xAxisLabel.setAttribute("y", (height + margin.bottom - 5).toString());
    xAxisLabel.setAttribute("text-anchor", "middle");
    xAxisLabel.setAttribute("font-size", "12");
    xAxisLabel.setAttribute("fill", "#4A5568");
    xAxisLabel.setAttribute("font-weight", "bold");
    xAxisLabel.textContent = "Year";
    g.appendChild(xAxisLabel);
    
    // Y-axis label
    const yAxisLabel = document.createElementNS("http://www.w3.org/2000/svg", "text");
    yAxisLabel.setAttribute("transform", `rotate(-90)`);
    yAxisLabel.setAttribute("x", (-height / 2).toString());
    yAxisLabel.setAttribute("y", (-margin.left + 15).toString());
    yAxisLabel.setAttribute("text-anchor", "middle");
    yAxisLabel.setAttribute("font-size", "12");
    yAxisLabel.setAttribute("fill", "#4A5568");
    yAxisLabel.setAttribute("font-weight", "bold");
    yAxisLabel.textContent = "Job Index";
    g.appendChild(yAxisLabel);
    
    // Create x-axis
    const xAxis = document.createElementNS("http://www.w3.org/2000/svg", "g");
    xAxis.setAttribute("transform", `translate(0,${height})`);
    xAxis.setAttribute("class", "x-axis");
    g.appendChild(xAxis);
    
    // X-axis line
    const xAxisLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
    xAxisLine.setAttribute("x1", "0");
    xAxisLine.setAttribute("y1", "0");
    xAxisLine.setAttribute("x2", width.toString());
    xAxisLine.setAttribute("y2", "0");
    xAxisLine.setAttribute("stroke", "#718096");
    xAxis.appendChild(xAxisLine);
    
    // X-axis ticks
    years.filter((_, i) => i % 2 === 0).forEach(year => {
      const tick = document.createElementNS("http://www.w3.org/2000/svg", "g");
      tick.setAttribute("transform", `translate(${xScale(year)},0)`);
      
      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("y2", "6");
      line.setAttribute("stroke", "#718096");
      tick.appendChild(line);
      
      const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
      text.setAttribute("y", "9");
      text.setAttribute("dy", ".71em");
      text.setAttribute("text-anchor", "middle");
      text.setAttribute("font-size", "11");
      text.setAttribute("fill", "#4A5568");
      text.textContent = year.toString();
      tick.appendChild(text);
      
      xAxis.appendChild(tick);
    });
    
    // Create y-axis
    const yAxis = document.createElementNS("http://www.w3.org/2000/svg", "g");
    yAxis.setAttribute("class", "y-axis");
    g.appendChild(yAxis);
    
    // Y-axis line
    const yAxisLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
    yAxisLine.setAttribute("x1", "0");
    yAxisLine.setAttribute("y1", "0");
    yAxisLine.setAttribute("x2", "0");
    yAxisLine.setAttribute("y2", height.toString());
    yAxisLine.setAttribute("stroke", "#718096");
    yAxis.appendChild(yAxisLine);
    
    // Y-axis ticks
    Array.from({ length: yTicks }).forEach((_, i) => {
      const value = yMin + (yMax - yMin) * i / (yTicks - 1);
      const tick = document.createElementNS("http://www.w3.org/2000/svg", "g");
      tick.setAttribute("transform", `translate(0,${yScale(value)})`);
      
      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x2", "-6");
      line.setAttribute("stroke", "#718096");
      tick.appendChild(line);
      
      const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
      text.setAttribute("x", "-9");
      text.setAttribute("dy", ".32em");
      text.setAttribute("text-anchor", "end");
      text.setAttribute("font-size", "11");
      text.setAttribute("fill", "#4A5568");
      text.textContent = Math.round(value).toString();
      tick.appendChild(text);
      
      yAxis.appendChild(tick);
    });
    
    // Create area under lines for better visualization
    // Current job area
    const currentJobArea = document.createElementNS("http://www.w3.org/2000/svg", "path");
    let currentJobAreaPath = "";
    data.currentJob.data.forEach((d, i) => {
      const x = xScale(d.year);
      const y = yScale(d.jobs);
      if (i === 0) {
        currentJobAreaPath += `M${x},${height} L${x},${y}`;
      } else {
        currentJobAreaPath += `L${x},${y}`;
      }
    });
    // Complete the path back to the x-axis
    currentJobAreaPath += `L${xScale(data.currentJob.data[data.currentJob.data.length - 1].year)},${height} Z`;
    currentJobArea.setAttribute("d", currentJobAreaPath);
    currentJobArea.setAttribute("fill", "#FED7D7");
    currentJobArea.setAttribute("fill-opacity", "0.5");
    g.appendChild(currentJobArea);
    
    // Recommended job area
    const recommendedJobArea = document.createElementNS("http://www.w3.org/2000/svg", "path");
    let recommendedJobAreaPath = "";
    data.recommendedJob.data.forEach((d, i) => {
      const x = xScale(d.year);
      const y = yScale(d.jobs);
      if (i === 0) {
        recommendedJobAreaPath += `M${x},${height} L${x},${y}`;
      } else {
        recommendedJobAreaPath += `L${x},${y}`;
      }
    });
    // Complete the path back to the x-axis
    recommendedJobAreaPath += `L${xScale(data.recommendedJob.data[data.recommendedJob.data.length - 1].year)},${height} Z`;
    recommendedJobArea.setAttribute("d", recommendedJobAreaPath);
    recommendedJobArea.setAttribute("fill", "#C6F6D5");
    recommendedJobArea.setAttribute("fill-opacity", "0.5");
    g.appendChild(recommendedJobArea);
    
    // Create the line for current job
    const currentJobLine = document.createElementNS("http://www.w3.org/2000/svg", "path");
    let currentJobPath = "";
    data.currentJob.data.forEach((d, i) => {
      const x = xScale(d.year);
      const y = yScale(d.jobs);
      if (i === 0) {
        currentJobPath += `M${x},${y}`;
      } else {
        currentJobPath += `L${x},${y}`;
      }
    });
    currentJobLine.setAttribute("d", currentJobPath);
    currentJobLine.setAttribute("fill", "none");
    currentJobLine.setAttribute("stroke", "#F56565");
    currentJobLine.setAttribute("stroke-width", "3");
    currentJobLine.setAttribute("stroke-linecap", "round");
    currentJobLine.setAttribute("stroke-linejoin", "round");
    g.appendChild(currentJobLine);
    
    // Add data points for current job
    data.currentJob.data.forEach((d) => {
      const x = xScale(d.year);
      const y = yScale(d.jobs);
      
      const dataPoint = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      dataPoint.setAttribute("cx", x.toString());
      dataPoint.setAttribute("cy", y.toString());
      dataPoint.setAttribute("r", "4");
      dataPoint.setAttribute("fill", "#F56565");
      dataPoint.setAttribute("stroke", "#FFF");
      dataPoint.setAttribute("stroke-width", "1.5");
      
      // Add tooltip functionality
      const tooltip = document.createElementNS("http://www.w3.org/2000/svg", "title");
      tooltip.textContent = `${data.currentJob.name} (${d.year}): ${d.jobs}`;
      dataPoint.appendChild(tooltip);
      
      g.appendChild(dataPoint);
    });
    
    // Create the line for recommended job
    const recommendedJobLine = document.createElementNS("http://www.w3.org/2000/svg", "path");
    let recommendedJobPath = "";
    data.recommendedJob.data.forEach((d, i) => {
      const x = xScale(d.year);
      const y = yScale(d.jobs);
      if (i === 0) {
        recommendedJobPath += `M${x},${y}`;
      } else {
        recommendedJobPath += `L${x},${y}`;
      }
    });
    recommendedJobLine.setAttribute("d", recommendedJobPath);
    recommendedJobLine.setAttribute("fill", "none");
    recommendedJobLine.setAttribute("stroke", "#48BB78");
    recommendedJobLine.setAttribute("stroke-width", "3");
    recommendedJobLine.setAttribute("stroke-linecap", "round");
    recommendedJobLine.setAttribute("stroke-linejoin", "round");
    g.appendChild(recommendedJobLine);
    
    // Add data points for recommended job
    data.recommendedJob.data.forEach((d) => {
      const x = xScale(d.year);
      const y = yScale(d.jobs);
      
      const dataPoint = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      dataPoint.setAttribute("cx", x.toString());
      dataPoint.setAttribute("cy", y.toString());
      dataPoint.setAttribute("r", "4");
      dataPoint.setAttribute("fill", "#48BB78");
      dataPoint.setAttribute("stroke", "#FFF");
      dataPoint.setAttribute("stroke-width", "1.5");
      
      // Add tooltip functionality
      const tooltip = document.createElementNS("http://www.w3.org/2000/svg", "title");
      tooltip.textContent = `${data.recommendedJob.name} (${d.year}): ${d.jobs}`;
      dataPoint.appendChild(tooltip);
      
      g.appendChild(dataPoint);
    });
    
    // Add intersection point where the lines cross (if they do)
    let intersectionFound = false;
    
    for (let i = 0; i < data.currentJob.data.length - 1; i++) {
      for (let j = 0; j < data.recommendedJob.data.length - 1; j++) {
        const currentA = data.currentJob.data[i];
        const currentB = data.currentJob.data[i + 1];
        const recA = data.recommendedJob.data[j];
        const recB = data.recommendedJob.data[j + 1];
        
        // Skip if year ranges don't overlap
        if (!(Math.max(currentA.year, recA.year) <= Math.min(currentB.year, recB.year))) {
          continue;
        }
        
        // Simple line intersection check
        if ((currentA.jobs > recA.jobs && currentB.jobs < recB.jobs) || 
            (currentA.jobs < recA.jobs && currentB.jobs > recB.jobs)) {
          
          // Estimate the intersection point (approximate)
          const ratio = (recA.jobs - currentA.jobs) / ((currentB.jobs - currentA.jobs) - (recB.jobs - recA.jobs));
          const intersectYear = currentA.year + ratio * (currentB.year - currentA.year);
          const intersectJobs = currentA.jobs + ratio * (currentB.jobs - currentA.jobs);
          
          const x = xScale(intersectYear);
          const y = yScale(intersectJobs);
          
          // Draw intersection point
          const intersectionPoint = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          intersectionPoint.setAttribute("cx", x.toString());
          intersectionPoint.setAttribute("cy", y.toString());
          intersectionPoint.setAttribute("r", "6");
          intersectionPoint.setAttribute("fill", "#805AD5");
          intersectionPoint.setAttribute("stroke", "#FFF");
          intersectionPoint.setAttribute("stroke-width", "2");
          
          // Add tooltip for intersection point
          const tooltip = document.createElementNS("http://www.w3.org/2000/svg", "title");
          tooltip.textContent = `Crossover Point (${Math.round(intersectYear)}): ${Math.round(intersectJobs)}`;
          intersectionPoint.appendChild(tooltip);
          
          g.appendChild(intersectionPoint);
          
          // Add a label for the intersection
          const intersectionLabel = document.createElementNS("http://www.w3.org/2000/svg", "text");
          intersectionLabel.setAttribute("x", x.toString());
          intersectionLabel.setAttribute("y", (y - 10).toString());
          intersectionLabel.setAttribute("text-anchor", "middle");
          intersectionLabel.setAttribute("font-size", "10");
          intersectionLabel.setAttribute("font-weight", "bold");
          intersectionLabel.setAttribute("fill", "#805AD5");
          intersectionLabel.textContent = "Crossover";
          g.appendChild(intersectionLabel);
          
          intersectionFound = true;
          break;
        }
      }
      if (intersectionFound) break;
    }
    
    // Add legend
    const legendBox = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    legendBox.setAttribute("x", (width - 160).toString());
    legendBox.setAttribute("y", "5");
    legendBox.setAttribute("width", "155");
    legendBox.setAttribute("height", "60");
    legendBox.setAttribute("rx", "5");
    legendBox.setAttribute("ry", "5");
    legendBox.setAttribute("fill", "#F7FAFC");
    legendBox.setAttribute("stroke", "#E2E8F0");
    g.appendChild(legendBox);
    
    const legend = document.createElementNS("http://www.w3.org/2000/svg", "g");
    legend.setAttribute("transform", `translate(${width - 150},15)`);
    
    // Current job legend item
    const currentJobLegend = document.createElementNS("http://www.w3.org/2000/svg", "g");
    
    const currentJobLegendDot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    currentJobLegendDot.setAttribute("cx", "5");
    currentJobLegendDot.setAttribute("cy", "5");
    currentJobLegendDot.setAttribute("r", "5");
    currentJobLegendDot.setAttribute("fill", "#F56565");
    currentJobLegend.appendChild(currentJobLegendDot);
    
    const currentJobLegendText = document.createElementNS("http://www.w3.org/2000/svg", "text");
    currentJobLegendText.setAttribute("x", "15");
    currentJobLegendText.setAttribute("y", "9");
    currentJobLegendText.setAttribute("font-size", "12");
    currentJobLegendText.setAttribute("fill", "#4A5568");
    currentJobLegendText.textContent = data.currentJob.name;
    currentJobLegend.appendChild(currentJobLegendText);
    
    legend.appendChild(currentJobLegend);
    
    // Recommended job legend item
    const recommendedJobLegend = document.createElementNS("http://www.w3.org/2000/svg", "g");
    recommendedJobLegend.setAttribute("transform", "translate(0,25)");
    
    const recommendedJobLegendDot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    recommendedJobLegendDot.setAttribute("cx", "5");
    recommendedJobLegendDot.setAttribute("cy", "5");
    recommendedJobLegendDot.setAttribute("r", "5");
    recommendedJobLegendDot.setAttribute("fill", "#48BB78");
    recommendedJobLegend.appendChild(recommendedJobLegendDot);
    
    const recommendedJobLegendText = document.createElementNS("http://www.w3.org/2000/svg", "text");
    recommendedJobLegendText.setAttribute("x", "15");
    recommendedJobLegendText.setAttribute("y", "9");
    recommendedJobLegendText.setAttribute("font-size", "12");
    recommendedJobLegendText.setAttribute("fill", "#4A5568");
    recommendedJobLegendText.textContent = data.recommendedJob.name;
    recommendedJobLegend.appendChild(recommendedJobLegendText);
    
    legend.appendChild(recommendedJobLegend);
    
    // Add explanation text for the chart
    const explanationText = document.createElementNS("http://www.w3.org/2000/svg", "text");
    explanationText.setAttribute("x", "10");
    explanationText.setAttribute("y", "15");
    explanationText.setAttribute("font-size", "11");
    explanationText.setAttribute("fill", "#718096");
    explanationText.textContent = "Higher values = More jobs available";
    g.appendChild(explanationText);
    
    g.appendChild(legend);
    
    // Add the chart to the DOM
    if (chart) {
      chart.innerHTML = '';
      chart.appendChild(svg);
    }
  }
</script>

<!-- Add help text to make the chart more understandable -->
<div class="bg-white rounded-lg p-4">
  <div class="mb-2 flex items-center justify-between">
    <h3 class="text-lg font-medium text-gray-800">Job Market Trends (2020-2030)</h3>
    <div class="flex items-center">
      <button class="text-gray-500 hover:text-gray-700 ml-2 text-sm bg-gray-100 hover:bg-gray-200 py-1 px-2 rounded-md" title="What am I looking at?">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        Help
      </button>
    </div>
  </div>
  
  <div class="text-sm text-gray-500 mb-2">
    <span class="font-medium">What this shows:</span> The expected number of jobs available over time for your current career vs recommended green job.
  </div>
  
  <div bind:this={chart} class="w-full h-64 overflow-hidden"></div>
  
  <div class="mt-4 bg-blue-50 p-3 rounded-md text-sm text-blue-700 border-l-4 border-blue-500">
    <strong>Key insight:</strong> The purple "Crossover" point shows when green jobs are expected to outnumber your current career jobs. This is when your reskilling investment could really pay off!
  </div>
</div>

<style>
  /* Add some styling for better accessibility */
  /* .job-trends-chart text {
    font-family: system-ui, -apple-system, sans-serif;
  } */
  
  /* Make interactive elements more obvious on hover */
  /* circle:hover {
    stroke-width: 3px;
    cursor: pointer;
  } */
</style>