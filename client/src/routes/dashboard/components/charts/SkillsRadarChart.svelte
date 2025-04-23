<script lang="ts">
  import { onMount } from 'svelte';
  
  export let skills: {
    name: string;
    value: number;
    relevance?: string;
    gap?: number;
  }[];
  
  export let chartType: 'current' | 'required' = 'current';
  export let showLegend: boolean = true;
  
  let chart: HTMLDivElement | null = null;
  
  onMount(() => {
    renderChart();
    
    // Handle window resize for responsiveness
    const handleResize = () => {
      if (chart) {
        renderChart();
      }
    };
    
    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  });
  
  function renderChart() {
    if (!chart) return;
    
    // Make chart size responsive to container
    const containerWidth = chart.clientWidth;
    const containerHeight = chart.clientHeight;
    const size = Math.min(containerWidth, containerHeight, 300);
    
    const width = size;
    const height = size;
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) / 2 - 40; // Increased padding for labels
    
    // Create SVG
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", "100%");
    svg.setAttribute("height", "100%");
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    
    // Add title for accessibility
    const title = document.createElementNS("http://www.w3.org/2000/svg", "title");
    title.textContent = chartType === 'current' ? "Current Skills Radar Chart" : "Required Skills and Gaps Radar Chart";
    svg.appendChild(title);
    
    // Add description for accessibility
    const desc = document.createElementNS("http://www.w3.org/2000/svg", "desc");
    desc.textContent = chartType === 'current' 
      ? "Radar chart showing current skill levels with relevance indicators" 
      : "Radar chart showing required skill levels and skill gaps";
    svg.appendChild(desc);
    
    // Create background circles with labels
    const circles = [0.2, 0.4, 0.6, 0.8, 1];
    circles.forEach((ratio, index) => {
      const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      circle.setAttribute("cx", centerX.toString());
      circle.setAttribute("cy", centerY.toString());
      circle.setAttribute("r", (radius * ratio).toString());
      circle.setAttribute("fill", "none");
      circle.setAttribute("stroke", "#E2E8F0");
      circle.setAttribute("stroke-width", "1");
      svg.appendChild(circle);
      
      // Add percentage labels to the top point of each circle
      if (index % 2 === 0) { // Add labels to every other circle for clarity
        const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
        label.setAttribute("x", centerX.toString());
        label.setAttribute("y", (centerY - radius * ratio - 2).toString());
        label.setAttribute("text-anchor", "middle");
        label.setAttribute("font-size", "8");
        label.setAttribute("fill", "#718096");
        label.textContent = `${ratio * 100}%`;
        svg.appendChild(label);
      }
    });
    
    // Create axes
    const angleStep = (2 * Math.PI) / skills.length;
    skills.forEach((skill, i) => {
      const angle = i * angleStep;
      const x = centerX + radius * Math.sin(angle);
      const y = centerY - radius * Math.cos(angle);
      
      const axis = document.createElementNS("http://www.w3.org/2000/svg", "line");
      axis.setAttribute("x1", centerX.toString());
      axis.setAttribute("y1", centerY.toString());
      axis.setAttribute("x2", x.toString());
      axis.setAttribute("y2", y.toString());
      axis.setAttribute("stroke", "#CBD5E0");
      axis.setAttribute("stroke-width", "1");
      svg.appendChild(axis);
      
      // Add skill labels with better positioning and background for readability
      const labelDistance = radius + 20;
      const labelX = centerX + labelDistance * Math.sin(angle);
      const labelY = centerY - labelDistance * Math.cos(angle);
      
      // Create a background for the label
      const labelBg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
      labelBg.setAttribute("x", (labelX - 30).toString());
      labelBg.setAttribute("y", (labelY - 10).toString());
      labelBg.setAttribute("width", "60");
      labelBg.setAttribute("height", "15");
      labelBg.setAttribute("rx", "3");
      labelBg.setAttribute("ry", "3");
      labelBg.setAttribute("fill", "white");
      labelBg.setAttribute("fill-opacity", "0.8");
      svg.appendChild(labelBg);
      
      // Add the label text
      const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
      label.setAttribute("x", labelX.toString());
      label.setAttribute("y", labelY.toString());
      label.setAttribute("text-anchor", "middle");
      label.setAttribute("font-size", "9");
      label.setAttribute("font-weight", "500");
      label.setAttribute("fill", "#2D3748");
      label.textContent = skill.name;
      svg.appendChild(label);
      
      // Add value labels
      const valueLabel = document.createElementNS("http://www.w3.org/2000/svg", "text");
      const valueX = centerX + (radius * skill.value / 100 * 0.85) * Math.sin(angle);
      const valueY = centerY - (radius * skill.value / 100 * 0.85) * Math.cos(angle);
      valueLabel.setAttribute("x", valueX.toString());
      valueLabel.setAttribute("y", valueY.toString());
      valueLabel.setAttribute("text-anchor", "middle");
      valueLabel.setAttribute("font-size", "8");
      valueLabel.setAttribute("font-weight", "bold");
      valueLabel.setAttribute("fill", chartType === 'current' ? "#2C7A7B" : "#2B6CB0");
      valueLabel.textContent = `${skill.value}%`;
      svg.appendChild(valueLabel);
    });
    
    // Create polygon for current skills
    let points = "";
    skills.forEach((skill, i) => {
      const angle = i * angleStep;
      const value = skill.value / 100; // Normalize to 0-1
      const x = centerX + radius * value * Math.sin(angle);
      const y = centerY - radius * value * Math.cos(angle);
      
      if (i === 0) {
        points += `${x},${y}`;
      } else {
        points += ` ${x},${y}`;
      }
      
      // Add enhanced dots at data points
      const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      dot.setAttribute("cx", x.toString());
      dot.setAttribute("cy", y.toString());
      dot.setAttribute("r", "4"); // Slightly larger dots
      
      // Determine colors based on chart type and relevance
      let fillColor = "#48BB78";
      if (chartType === 'current') {
        if (skill.relevance === 'High') {
          fillColor = "#2C7A7B"; // teal-600
        } else if (skill.relevance === 'Medium') {
          fillColor = "#D69E2E"; // yellow-600
        } else {
          fillColor = "#718096"; // gray-500
        }
      } else {
        fillColor = "#2B6CB0"; // blue-600
      }
      
      dot.setAttribute("fill", fillColor);
      
      // Add stroke for better visibility
      dot.setAttribute("stroke", "white");
      dot.setAttribute("stroke-width", "1");
      
      svg.appendChild(dot);
    });
    
    // Create polygon for skills area
    const polygon = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
    polygon.setAttribute("points", points);
    
    if (chartType === 'current') {
      polygon.setAttribute("fill", "rgba(56, 178, 172, 0.3)"); // teal-500 with transparency
      polygon.setAttribute("stroke", "#38B2AC"); // teal-500
    } else {
      polygon.setAttribute("fill", "rgba(66, 153, 225, 0.3)"); // blue-500 with transparency
      polygon.setAttribute("stroke", "#4299E1"); // blue-500
    }
    
    polygon.setAttribute("stroke-width", "2");
    svg.insertBefore(polygon, svg.firstChild);
    
    // If this is the required skills chart, add the gap visualization
    if (chartType === 'required' && skills[0].gap !== undefined) {
      let gapPoints = "";
      skills.forEach((skill, i) => {
        const angle = i * angleStep;
        const value = (skill.value - (skill.gap ?? 0)) / 100; // Normalize to 0-1
        const x = centerX + radius * value * Math.sin(angle);
        const y = centerY - radius * value * Math.cos(angle);
        
        if (i === 0) {
          gapPoints += `${x},${y}`;
        } else {
          gapPoints += ` ${x},${y}`;
        }
        
        // Add dots for current skill level (with gaps)
        const gapDot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        gapDot.setAttribute("cx", x.toString());
        gapDot.setAttribute("cy", y.toString());
        gapDot.setAttribute("r", "3");
        gapDot.setAttribute("fill", "#A0AEC0"); // gray-400
        gapDot.setAttribute("stroke", "white");
        gapDot.setAttribute("stroke-width", "1");
        svg.appendChild(gapDot);
      });
      
      // Create polygon for current skill levels
      const gapPolygon = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
      gapPolygon.setAttribute("points", gapPoints);
      gapPolygon.setAttribute("fill", "rgba(160, 174, 192, 0.3)"); // gray-400 with transparency
      gapPolygon.setAttribute("stroke", "#A0AEC0"); // gray-400
      gapPolygon.setAttribute("stroke-width", "1.5");
      gapPolygon.setAttribute("stroke-dasharray", "3,2");
      svg.insertBefore(gapPolygon, svg.firstChild);
    }
    
    // Add the chart to the DOM
    if (chart) {
      chart.innerHTML = '';
      chart.appendChild(svg);
      
      // Add legend if enabled
      if (showLegend) {
        const legend = document.createElement('div');
        legend.style.display = 'flex';
        legend.style.justifyContent = 'center';
        legend.style.flexWrap = 'wrap';
        legend.style.gap = '12px';
        legend.style.marginTop = '10px';
        
        if (chartType === 'current') {
          // Legend for current skills
          const highItem = createLegendItem('#2C7A7B', 'High Relevance');
          const medItem = createLegendItem('#D69E2E', 'Medium Relevance');
          const lowItem = createLegendItem('#718096', 'Low Relevance');
          
          legend.appendChild(highItem);
          legend.appendChild(medItem);
          legend.appendChild(lowItem);
        } else {
          // Legend for required skills
          const requiredItem = createLegendItem('#2B6CB0', 'Required Skill Level');
          const currentItem = createLegendItem('#A0AEC0', 'Current Skill Level');
          
          legend.appendChild(requiredItem);
          legend.appendChild(currentItem);
        }
        
        chart.appendChild(legend);
      }
    }
  }
  
  function createLegendItem(color: string, label: string): HTMLDivElement {
    const item = document.createElement('div');
    item.style.display = 'flex';
    item.style.alignItems = 'center';
    item.style.fontSize = '10px';
    
    const colorBox = document.createElement('div');
    colorBox.style.width = '10px';
    colorBox.style.height = '10px';
    colorBox.style.backgroundColor = color;
    colorBox.style.marginRight = '4px';
    colorBox.style.borderRadius = '2px';
    
    const labelText = document.createElement('span');
    labelText.textContent = label;
    labelText.style.color = '#4A5568';
    
    item.appendChild(colorBox);
    item.appendChild(labelText);
    
    return item;
  }
</script>

<div class="radar-chart-container">
  <div bind:this={chart} class="w-full h-full flex flex-col items-center justify-center min-h-48"></div>
  
  {#if chartType === 'required'}
    <div class="text-center mt-2 text-sm text-gray-500">
      <p class="text-xs">The filled area shows required skills, the dashed area shows your current skills.</p>
    </div>
  {/if}
</div>

<style>
  .radar-chart-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    min-height: 220px;
  }
</style>