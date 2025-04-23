<script lang="ts">
  import { onMount } from 'svelte';
  
  export let data: {
    name: string;
    sustainability: number;
    futureProof: number;
    salary: number;
  }[];
  
  let chart: HTMLElement;
  let tooltip: HTMLElement;
  let tooltipVisible = false;
  let tooltipContent = { title: '', value: '', metric: '' };
  let tooltipPosition = { x: 0, y: 0 };
  
  // Colors with better contrast
  const colors = {
    sustainability: '#10B981', // Green that's vibrant but not too bright
    futureProof: '#3B82F6',    // Blue that stands out clearly
    salary: '#F59E0B',         // Amber that's visible but not harsh
    grid: '#E5E7EB',           // Light gray for grid lines
    text: '#374151'            // Dark gray for text
  };
  
  // Labels for metrics (more descriptive)
  const metricLabels = {
    sustainability: 'Environmental Impact',
    futureProof: 'Automation Resistance',
    salary: 'Earning Potential'
  };
  
  onMount(() => {
    renderChart();
    window.addEventListener('resize', renderChart);
    return () => window.removeEventListener('resize', renderChart);
  });

  function renderChart() {
    const containerWidth = chart.clientWidth;
    // Responsive dimensions
    const width = Math.min(containerWidth, 800);
    const height = Math.min(250, width * 0.6);
    const margin = { 
      top: 50, 
      right: Math.max(100, width * 0.2), 
      bottom: 40, 
      left: Math.max(120, width * 0.25) 
    };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    // Build SVG from scratch
    chart.innerHTML = '';
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", width.toString());
    svg.setAttribute("height", height.toString());
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.setAttribute("class", "font-sans");
    
    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
    g.setAttribute("transform", `translate(${margin.left},${margin.top})`);
    svg.appendChild(g);
    
    // Y scale (job names)
    const yScale = (index: number) => index * (innerHeight / (data.length - 1 || 1));
    
    // X scale (metrics)
    const xScale = (value: number) => (value / 100) * innerWidth;
    
    // Create axes and grid
    createGrid(g, innerWidth, innerHeight, xScale);
    
    // Add title with clear hierarchy
    const title = document.createElementNS("http://www.w3.org/2000/svg", "text");
    title.setAttribute("x", (width / 2).toString());
    title.setAttribute("y", "24");
    title.setAttribute("text-anchor", "middle");
    title.setAttribute("font-size", "16");
    title.setAttribute("font-weight", "bold");
    title.setAttribute("fill", colors.text);
    title.textContent = "Job Comparison";
    svg.appendChild(title);
    
    // Add subtitle with more context
    const subtitle = document.createElementNS("http://www.w3.org/2000/svg", "text");
    subtitle.setAttribute("x", (width / 2).toString());
    subtitle.setAttribute("y", "42");
    subtitle.setAttribute("text-anchor", "middle");
    subtitle.setAttribute("font-size", "12");
    subtitle.setAttribute("fill", colors.text);
    subtitle.textContent = "Higher scores are better (scale: 0-100)";
    svg.appendChild(subtitle);

    // Create job rows
    data.forEach((job, i) => {
      const y = yScale(i);
      
      // Job label with background for better readability
      const labelBg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
      labelBg.setAttribute("x", (-margin.left + 5).toString());
      labelBg.setAttribute("y", (y - 10).toString());
      labelBg.setAttribute("width", (margin.left - 10).toString());
      labelBg.setAttribute("height", "20");
      labelBg.setAttribute("fill", "#F9FAFB");
      labelBg.setAttribute("rx", "3");
      g.appendChild(labelBg);
      
      const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
      text.setAttribute("x", (-10).toString());
      text.setAttribute("y", y.toString());
      text.setAttribute("dy", ".32em");
      text.setAttribute("text-anchor", "end");
      text.setAttribute("font-size", "12");
      text.setAttribute("font-weight", i === 0 ? "bold" : "normal"); // Highlight current job
      text.setAttribute("fill", colors.text);
      text.textContent = job.name;
      g.appendChild(text);
      
      // Horizontal line for this job row
      const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
      line.setAttribute("x1", "0");
      line.setAttribute("y1", y.toString());
      line.setAttribute("x2", innerWidth.toString());
      line.setAttribute("y2", y.toString());
      line.setAttribute("stroke", i % 2 === 0 ? "#F3F4F6" : "transparent");
      line.setAttribute("stroke-width", "8");
      g.insertBefore(line, g.firstChild);
      
      // Create dots and connector line
      const points = [
        { metric: 'sustainability' as keyof typeof metricLabels, value: job.sustainability, color: colors.sustainability, x: xScale(job.sustainability), y },
        { metric: 'futureProof' as keyof typeof metricLabels, value: job.futureProof, color: colors.futureProof, x: xScale(job.futureProof), y },
        { metric: 'salary' as keyof typeof metricLabels, value: job.salary, color: colors.salary, x: xScale(job.salary), y }
      ];
      
      // Add connecting line between metrics
      const lineGenerator = document.createElementNS("http://www.w3.org/2000/svg", "path");
      const lineData = `M${points[0].x},${points[0].y} L${points[1].x},${points[1].y} L${points[2].x},${points[2].y}`;
      lineGenerator.setAttribute("d", lineData);
      lineGenerator.setAttribute("fill", "none");
      lineGenerator.setAttribute("stroke", "#9CA3AF");
      lineGenerator.setAttribute("stroke-width", "1");
      lineGenerator.setAttribute("stroke-dasharray", "3,2");
      lineGenerator.setAttribute("opacity", "0.6");
      g.appendChild(lineGenerator);
      
      // Add dots for each metric
      points.forEach(point => {
        // Add value label for clarity
        const valueText = document.createElementNS("http://www.w3.org/2000/svg", "text");
        valueText.setAttribute("x", point.x.toString());
        valueText.setAttribute("y", (point.y - 15).toString());
        valueText.setAttribute("text-anchor", "middle");
        valueText.setAttribute("font-size", "10");
        valueText.setAttribute("fill", point.color);
        valueText.textContent = point.value.toString();
        g.appendChild(valueText);
        
        // Create interactive dot
        const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        dot.setAttribute("cx", point.x.toString());
        dot.setAttribute("cy", point.y.toString());
        dot.setAttribute("r", "7");
        dot.setAttribute("fill", point.color);
        dot.setAttribute("stroke", "white");
        dot.setAttribute("stroke-width", "2");
        dot.setAttribute("class", "job-metric-dot");
        
        // Interactive events for dots
        dot.addEventListener('mouseover', (e) => {
          dot.setAttribute("r", "9"); // Enlarge on hover
          
          // Show tooltip
          tooltipContent = {
            title: job.name,
            value: point.value.toString(),
            metric: metricLabels[point.metric]
          };
          
          // Position tooltip
          const svgRect = svg.getBoundingClientRect();
          const dotRect = dot.getBoundingClientRect();
          tooltipPosition = {
            x: dotRect.left - svgRect.left + dotRect.width/2,
            y: dotRect.top - svgRect.top
          };
          tooltipVisible = true;
        });
        
        dot.addEventListener('mouseout', () => {
          dot.setAttribute("r", "7"); // Reset size
          tooltipVisible = false;
        });
        
        g.appendChild(dot);
      });
    });
    
    // Add legend
    addLegend(g, innerWidth, margin);
    
    // Add the chart to the DOM
    chart.appendChild(svg);
  }
  
  function createGrid(g: SVGGElement, innerWidth: number, innerHeight: number, xScale: (value: number) => number) {
    // X-axis line
    const xAxisLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
    xAxisLine.setAttribute("x1", "0");
    xAxisLine.setAttribute("y1", innerHeight.toString());
    xAxisLine.setAttribute("x2", innerWidth.toString());
    xAxisLine.setAttribute("y2", innerHeight.toString());
    xAxisLine.setAttribute("stroke", colors.text);
    g.appendChild(xAxisLine);
    
    // X-axis ticks with labels
    const xTicks = [0, 25, 50, 75, 100];
    xTicks.forEach(tick => {
      const x = xScale(tick);
      
      // Grid line
      const gridLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
      gridLine.setAttribute("x1", x.toString());
      gridLine.setAttribute("y1", "0");
      gridLine.setAttribute("x2", x.toString());
      gridLine.setAttribute("y2", innerHeight.toString());
      gridLine.setAttribute("stroke", colors.grid);
      gridLine.setAttribute("stroke-width", "1");
      g.insertBefore(gridLine, g.firstChild);
      
      // Tick mark
      const tickMark = document.createElementNS("http://www.w3.org/2000/svg", "line");
      tickMark.setAttribute("x1", x.toString());
      tickMark.setAttribute("y1", innerHeight.toString());
      tickMark.setAttribute("x2", x.toString());
      tickMark.setAttribute("y2", (innerHeight + 6).toString());
      tickMark.setAttribute("stroke", colors.text);
      g.appendChild(tickMark);
      
      // Tick label
      const tickLabel = document.createElementNS("http://www.w3.org/2000/svg", "text");
      tickLabel.setAttribute("x", x.toString());
      tickLabel.setAttribute("y", (innerHeight + 20).toString());
      tickLabel.setAttribute("text-anchor", "middle");
      tickLabel.setAttribute("font-size", "11");
      tickLabel.setAttribute("fill", colors.text);
      tickLabel.textContent = tick.toString();
      g.appendChild(tickLabel);
    });
  }
  
  function addLegend(g: SVGGElement, innerWidth: number, margin: { top: number; right: number; bottom: number; left: number }) {
    const legend = document.createElementNS("http://www.w3.org/2000/svg", "g");
    legend.setAttribute("transform", `translate(${innerWidth + 20}, 10)`);
    
    const legendItems = [
      { color: colors.sustainability, label: metricLabels.sustainability },
      { color: colors.futureProof, label: metricLabels.futureProof },
      { color: colors.salary, label: metricLabels.salary }
    ];
    
    // Add legend title
    const legendTitle = document.createElementNS("http://www.w3.org/2000/svg", "text");
    legendTitle.setAttribute("x", "0");
    legendTitle.setAttribute("y", "-5");
    legendTitle.setAttribute("font-size", "12");
    legendTitle.setAttribute("font-weight", "bold");
    legendTitle.setAttribute("fill", colors.text);
    legendTitle.textContent = "Metrics";
    legend.appendChild(legendTitle);
    
    legendItems.forEach((item, i) => {
      const legendGroup = document.createElementNS("http://www.w3.org/2000/svg", "g");
      legendGroup.setAttribute("transform", `translate(0, ${i * 25 + 15})`);
      
      // Legend dot
      const legendDot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      legendDot.setAttribute("cx", "8");
      legendDot.setAttribute("cy", "8");
      legendDot.setAttribute("r", "6");
      legendDot.setAttribute("fill", item.color);
      legendDot.setAttribute("stroke", "white");
      legendDot.setAttribute("stroke-width", "1.5");
      legendGroup.appendChild(legendDot);
      
      // Legend text
      const legendText = document.createElementNS("http://www.w3.org/2000/svg", "text");
      legendText.setAttribute("x", "20");
      legendText.setAttribute("y", "12");
      legendText.setAttribute("font-size", "12");
      legendText.setAttribute("fill", colors.text);
      legendText.textContent = item.label;
      legendGroup.appendChild(legendText);
      
      legend.appendChild(legendGroup);
    });
    
    g.appendChild(legend);
  }
  
  function handleTooltipClick() {
    tooltipVisible = false;
  }
</script>

<div class="relative w-full h-full">
  <div bind:this={chart} class="w-full h-full"></div>
  
  <!-- Tooltip -->
  {#if tooltipVisible}
    <button 
      bind:this={tooltip}
      class="absolute bg-white p-2 rounded shadow-lg border border-gray-200 text-sm z-10"
      style="left: {tooltipPosition.x}px; top: {tooltipPosition.y - 70}px; transform: translateX(-50%);"
      on:click={handleTooltipClick}
      aria-label="Tooltip: {tooltipContent.title}, {tooltipContent.metric} {tooltipContent.value}/100"
    >
      <div class="font-bold text-gray-700">{tooltipContent.title}</div>
      <div class="flex justify-between gap-2">
        <span class="text-gray-600">{tooltipContent.metric}:</span>
        <span class="font-semibold">{tooltipContent.value}/100</span>
      </div>
      <div class="text-xs text-gray-500 text-center mt-1">(Click to close)</div>
      
      <!-- Tooltip arrow -->
      <div class="absolute w-3 h-3 bg-white border-r border-b border-gray-200 transform rotate-45 left-1/2 -bottom-1.5 -ml-1.5"></div>
    </button>
  {/if}
  
  <!-- Mobile-friendly legend for small screens -->
  <div class="md:hidden mt-4 flex flex-wrap justify-center gap-4 text-sm">
    <div class="flex items-center">
      <span class="inline-block w-3 h-3 rounded-full bg-green-500 mr-1"></span>
      <span>Environmental Impact</span>
    </div>
    <div class="flex items-center">
      <span class="inline-block w-3 h-3 rounded-full bg-blue-500 mr-1"></span>
      <span>Automation Resistance</span>
    </div>
    <div class="flex items-center">
      <span class="inline-block w-3 h-3 rounded-full bg-amber-500 mr-1"></span>
      <span>Earning Potential</span>
    </div>
  </div>
</div>

<style>
  /* .job-metric-dot {
    cursor: pointer;
    transition: r 0.2s ease;
  } */
</style>