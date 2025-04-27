<!-- STAGE 1: STEMS AND LEAVES - Enhanced for realism -->
<script lang="ts">
    import { onMount } from 'svelte';
    import { tweened } from 'svelte/motion';
    import { cubicOut, elasticOut } from 'svelte/easing';
    
    // Growth sequence variables - separated for staggered growth
    const mainStemGrowth = tweened(0, { duration: 2200, easing: cubicOut });
    const sideStemGrowth = tweened(0, { duration: 1800, easing: cubicOut });
    const leafUnfurl = tweened(0, { duration: 2500, easing: elasticOut });
    
    // Colors
    const stemBaseColor = "#3e642c";
    const stemTipColor = "#85b053";
    const leafDarkColor = "#2d5016";
    const leafLightColor = "#a7d66c";
    
    // Wind effects
    let time = 0;
    let windStrength = 0.4; // Base wind strength
    let windGusts = 0; // Additional random gusts
    
    // Wind effect calculation with micro-oscillations
    function calculateWindEffect(seedValue: number, maxDegrees: number) {
      // Base wind effect
      const baseWind = Math.sin(time * 0.001 + seedValue) * maxDegrees * windStrength;
      
      // Micro-oscillations (tiny wiggles)
      const microWiggle = Math.sin(time * 0.005 + seedValue * 2) * 1.2;
      
      // Random gusts occasionally
      const gust = windGusts * Math.sin(time * 0.0015 + seedValue * 3) * 2;
      
      return baseWind + microWiggle + gust;
    }
  
    // Leaf breathing animation (subtle scale)
    function calculateLeafBreathing(seedValue: number) {
      // Only apply breathing once leaves are fully unfurled
      if ($leafUnfurl < 0.95) return 1;
      
      // Subtle breathing effect
      return 1 + Math.sin(time * 0.0008 + seedValue) * 0.015;
    }
    
    // Start the growth sequence with staggered timing
    onMount(() => {
      // Animation loop for continuous effects
      const interval = setInterval(() => {
        time += 16; // ~60fps
        
        // Random wind gusts
        if (Math.random() < 0.005) {
          windGusts = Math.random() * 0.6;
          setTimeout(() => windGusts = 0, 2000); // Gust lasts 2 seconds
        }
      }, 16);
      
      // Staggered growth sequence
      setTimeout(() => mainStemGrowth.set(1), 100);
      setTimeout(() => sideStemGrowth.set(1), 1400);
      setTimeout(() => leafUnfurl.set(1), 2200);
      
      return () => clearInterval(interval);
    });
  </script>
  
  <svg viewBox="100 240 100 120" width="100%" height="100%">
    <!-- Create gradient definitions with more natural color transitions -->
    <defs>
      <linearGradient id="stemGradient1" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="10%" stop-color={stemBaseColor} />
        <stop offset="80%" stop-color={stemTipColor} />
        <stop offset="95%" stop-color="#a1c16a" /> <!-- Slightly lighter tip -->
      </linearGradient>
      
      <linearGradient id="leafGradient1" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="10%" stop-color={leafDarkColor} />
        <stop offset="70%" stop-color={leafLightColor} />
        <stop offset="95%" stop-color="#c6e99c" /> <!-- Highlight on edge -->
      </linearGradient>
      
      <!-- Texture filter for slightly organic look -->
      <filter id="organicTexture" x="-20%" y="-20%" width="140%" height="140%">
        <feTurbulence type="fractalNoise" baseFrequency="0.15" numOctaves="2" seed="5" result="noise" />
        <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5" />
      </filter>
    </defs>
    
    <!-- Ground shadow that grows with the plant -->
    <ellipse 
      cx="150" 
      cy="350" 
      rx={20 + $mainStemGrowth * 15} 
      ry={3 + $mainStemGrowth * 2} 
      fill="#00000020"
      style="transform-origin: center; transform: scaleX({1 + Math.sin(time * 0.001) * 0.03});"
    />
          
    <!-- Main plant structure -->
    <g style="transform-origin: bottom;">
      <!-- Main Stem - more natural curve with variable thickness -->
      <path 
        d="M150 350 C151 330, 148 310, 152 300 C156 290, 150 280, 150 270" 
        stroke="url(#stemGradient1)" 
        stroke-width="4"
        stroke-linecap="round"
        fill="none"
        style="
          transform: rotate({calculateWindEffect(2, 3)}deg); 
          transform-origin: bottom;
          transform-box: fill-box;
          stroke-dasharray: 150;
          stroke-dashoffset: {150 - (150 * $mainStemGrowth)};
          opacity: {$mainStemGrowth};
        "
        class="transition-all duration-300"
      />
      
      <!-- Stem texture/detail -->
      <path 
        d="M150 350 C151 335, 149.5 320, 151.5 310" 
        stroke="#56883a" 
        stroke-width="1"
        stroke-linecap="round"
        fill="none"
        style="
          transform: rotate({calculateWindEffect(2, 3)}deg); 
          transform-origin: bottom;
          stroke-dasharray: 70;
          stroke-dashoffset: {70 - (70 * $mainStemGrowth)};
          opacity: {$mainStemGrowth * 0.6};
        "
      />
        
      <!-- Side Stems with variable thickness and natural curves -->
      <path 
        d="M150 320 C155 318, 160 315, 167 312 C174 309, 177 305, 175 305" 
        stroke="url(#stemGradient1)" 
        stroke-width="2"
        stroke-linecap="round"
        fill="none"
        style="
          transform: rotate({calculateWindEffect(4, 5)}deg); 
          transform-origin: 150px 320px;
          stroke-dasharray: 40;
          stroke-dashoffset: {40 - (40 * $sideStemGrowth)};
          opacity: {$sideStemGrowth};
        "
        class="transition-all duration-500"
      />
      
      <path 
        d="M152 300 C145 296, 138 293, 132 288 C126 283, 123 280, 125 285" 
        stroke="url(#stemGradient1)" 
        stroke-width="2"
        stroke-linecap="round"
        fill="none"
        style="
          transform: rotate({calculateWindEffect(3, 7)}deg); 
          transform-origin: 152px 300px;
          stroke-dasharray: 40;
          stroke-dashoffset: {40 - (40 * $sideStemGrowth)};
          opacity: {$sideStemGrowth};
        "
        class="transition-all duration-600"
      />
      
      <!-- Organic shaped leaves with breathing and texture -->
      <!-- Right leaf cluster -->
      <g style="transform-origin: 175px 305px;">
        <path 
          d="M175 305 C180 303, 187 302, 193 306 C198 310, 199 316, 195 320 C191 324, 182 323, 177 319 C172 315, 172 308, 175 305 Z" 
          fill="url(#leafGradient1)"
          stroke={leafDarkColor}
          stroke-width="0.8"
          filter="url(#organicTexture)"
          style="
            transform: rotate({calculateWindEffect(5, 8)}deg) scale({0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(1)}, {0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(1)});
            opacity: {$leafUnfurl};
          "
          class="transition-all duration-700"
        />
        
        <!-- Leaf veins for the right leaf - with varied thickness -->
        <path 
          d="M175 305 C179 308, 183 311, 188 315" 
          stroke={leafDarkColor} 
          stroke-width="0.6"
          style="
            transform: rotate({calculateWindEffect(5, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.6};
          "
        />
        
        <path 
          d="M175 305 C181 309, 188 313, 193 314" 
          stroke={leafDarkColor} 
          stroke-width="0.4"
          style="
            transform: rotate({calculateWindEffect(5.5, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.5};
          "
        />
        
        <path 
          d="M175 305 C179 307, 184 315, 190 317" 
          stroke={leafDarkColor} 
          stroke-width="0.3"
          style="
            transform: rotate({calculateWindEffect(5.2, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.4};
          "
        />
      </g>
      
      <!-- Left leaf cluster -->
      <g style="transform-origin: 125px 285px;">
        <path 
          d="M125 285 C120 282, 112 281, 106 284 C100 288, 98 295, 102 300 C106 305, 117 304, 124 299 C130 294, 128 288, 125 285 Z" 
          fill="url(#leafGradient1)"
          stroke={leafDarkColor}
          stroke-width="0.8"
          filter="url(#organicTexture)"
          style="
            transform: rotate({calculateWindEffect(6, 9)}deg) scale({0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(2)}, {0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(2)});
            opacity: {$leafUnfurl};
          "
          class="transition-all duration-800"
        />
        
        <!-- Leaf veins for the left leaf - with varied thickness and position -->
        <path 
          d="M125 285 C120 288, 114 291, 108 293" 
          stroke={leafDarkColor} 
          stroke-width="0.6"
          style="
            transform: rotate({calculateWindEffect(6, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.6};
          "
        />
        
        <path 
          d="M125 285 C117 289, 111 294, 105 297" 
          stroke={leafDarkColor} 
          stroke-width="0.4"
          style="
            transform: rotate({calculateWindEffect(6.3, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.5};
          "
        />
        
        <path 
          d="M125 285 C119 287, 112 295, 106 298" 
          stroke={leafDarkColor} 
          stroke-width="0.3"
          style="
            transform: rotate({calculateWindEffect(6.5, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.4};
          "
        />
      </g>
      
      <!-- Top leaves -->
      <g style="transform-origin: 150px 270px;">
        <path 
          d="M150 270 C156 264, 164 262, 169 267 C174 273, 172 279, 166 282 C159 284, 153 278, 150 270 Z" 
          fill="url(#leafGradient1)"
          stroke={leafDarkColor}
          stroke-width="0.8"
          filter="url(#organicTexture)"
          style="
            transform: rotate({calculateWindEffect(7, 10)}deg) scale({0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(3)}, {0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(3)});
            opacity: {$leafUnfurl};
          "
          class="transition-all duration-900"
        />
        
        <path 
          d="M150 270 C144 264, 136 262, 131 267 C126 273, 128 279, 134 282 C141 284, 147 278, 150 270 Z" 
          fill="url(#leafGradient1)"
          stroke={leafDarkColor}
          stroke-width="0.8"
          filter="url(#organicTexture)"
          style="
            transform: rotate({calculateWindEffect(6, 10)}deg) scale({0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(4)}, {0.2 + $leafUnfurl * 0.8 * calculateLeafBreathing(4)});
            opacity: {$leafUnfurl};
          "
          class="transition-all duration-1000"
        />
        
        <!-- Leaf veins for top leaves -->
        <path 
          d="M150 270 C156 271, 161 275, 166 279" 
          stroke={leafDarkColor} 
          stroke-width="0.5"
          style="
            transform: rotate({calculateWindEffect(7, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.5};
          "
        />
        
        <path 
          d="M150 270 C144 271, 139 275, 134 279" 
          stroke={leafDarkColor} 
          stroke-width="0.5"
          style="
            transform: rotate({calculateWindEffect(6, 5)}deg) scale({$leafUnfurl}, {$leafUnfurl});
            opacity: {$leafUnfurl * 0.5};
          "
        />
      </g>
    </g>
    
    <!-- Environmental elements: floating particles -->
    {#if $leafUnfurl > 0.5}
      <g>
        {#each Array(5) as _, i}
          <circle 
            cx={150 + Math.sin(time * 0.002 + i) * 20} 
            cy={300 - (time % 1000) * 0.05 - i * 10} 
            r={0.5 + Math.random() * 0.5}
            fill="#ffffff60"
            style="opacity: {Math.max(0, 1 - (time % 1000) * 0.001)};"
          />
        {/each}
      </g>
    {/if}
  </svg>