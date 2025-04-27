<script lang="ts">
    import { onMount, createEventDispatcher } from 'svelte';
    import { tweened } from 'svelte/motion';
    import { cubicOut, elasticOut, cubicInOut } from 'svelte/easing';
    import YoungPlant from '$lib/components/animations/YoungPlant.svelte';
    
    // Props
    export let autoTransition = true;
    export let initialStage = 0;
    export let windEffect = true;
    export let growthSpeed = 1.0; // Multiplier for growth speed
    
    // Component state
    let growthStage = initialStage; // 0: Sprout, 1: Stem/Leaves, 2: Small Tree, 3: Full Tree
    let mounted = false;
    let hovered = false;
    let clicked = false;
    let windActive = false;
    let shouldSway = false;
    
    // Animation controls
    const growthProgress = tweened(0, {
      duration: 2000 / growthSpeed,
      easing: elasticOut
    });
    
    const windStrength = tweened(0, {
      duration: 3000,
      easing: cubicOut
    });
    
    // Secondary animations
    const leafUnfurl = tweened(0, {
      duration: 1500 / growthSpeed,
      easing: cubicInOut
    });
    
    const groundMovement = tweened(0, {
      duration: 800,
      easing: cubicOut
    });
    
    // Event dispatcher
    const dispatch = createEventDispatcher();
    
    // Set up animations on mount
    onMount(() => {
      // Start with ground appearing and sprout emerging
      setTimeout(() => {
        mounted = true;
        groundMovement.set(1);
        
        setTimeout(() => {
          growthProgress.set(1);
          setTimeout(() => leafUnfurl.set(1), 300 / growthSpeed);
          
          // Start wind effect if enabled
          if (windEffect) {
            startWindEffect();
          }
          
          // Set up auto transitions if enabled
          if (autoTransition) {
            startAutoTransition();
          }
        }, 500);
      }, 300);
      
      return () => {
        // Clean up any intervals or timeouts
        shouldSway = false;
      };
    });
    
    function startWindEffect() {
      shouldSway = true;
      applyWindEffect();
    }
    
    function applyWindEffect() {
      if (!shouldSway) return;
      
      // Random wind strength
      windActive = true;
      const strength = Math.random() * 0.5 + 0.2;
      windStrength.set(strength, { duration: 2000 + Math.random() * 2000 });
      
      // Random delay before next sway
      setTimeout(() => {
        windStrength.set(0.1, { duration: 2000 + Math.random() * 1000 });
        setTimeout(() => {
          if (shouldSway) {
            applyWindEffect();
          }
        }, 1000 + Math.random() * 2000);
      }, 2000 + Math.random() * 3000);
    }
    
    function startAutoTransition() {
      setTimeout(() => {
        if (growthStage < 3) {
          growToNextStage();
          startAutoTransition();
        }
      }, 4000 / growthSpeed);
    }
    
    function handleClick() {
      clicked = true;
      setTimeout(() => clicked = false, 300);
      growToNextStage();
      dispatch('interaction', { stage: growthStage });
    }
    
    function growToNextStage() {
      if (growthStage < 3) {
        growthProgress.set(0);
        leafUnfurl.set(0);
        growthStage = (growthStage + 1) % 4;
        growthProgress.set(1);
        setTimeout(() => leafUnfurl.set(1), 300 / growthSpeed);
      } else {
        // Reset to sprout for a loop effect
        growthProgress.set(0);
        leafUnfurl.set(0);
        growthStage = 0;
        setTimeout(() => {
          growthProgress.set(1);
          setTimeout(() => leafUnfurl.set(1), 300 / growthSpeed);
        }, 100);
      }
    }
    
    function handleHover(isHovering: boolean) {
      hovered = isHovering;
    }
    
    // Helper function to calculate wind effect on elements
    $: calculateWindEffect = (baseAmount: number, height: number) => {
      // Wind affects higher parts more than the base
      const heightFactor = height * 0.01;
      return $windStrength * baseAmount * (1 + heightFactor);
    };
    
    // Color transitions based on growth stage with gradients
    $: stemBaseColor = growthStage === 0 ? "#2F855A" : 
                       growthStage === 1 ? "#276749" : 
                       growthStage === 2 ? "#22543D" : "#1C4532";
    
    $: stemTipColor = growthStage === 0 ? "#4ADE80" : 
                      growthStage === 1 ? "#34D399" : 
                      growthStage === 2 ? "#10B981" : "#059669";
    
    $: leafDarkColor = growthStage === 0 ? "#22C55E" : 
                       growthStage === 1 ? "#16A34A" : 
                       growthStage === 2 ? "#15803D" : "#166534";
                       
    $: leafLightColor = growthStage === 0 ? "#4ADE80" : 
                        growthStage === 1 ? "#34D399" : 
                        growthStage === 2 ? "#10B981" : "#059669";
                        
    $: fruitColor = "#F97316";
    $: fruitHighlightColor = "#FBBF24";
  </script>
  
  <div 
    class="plant-container relative cursor-pointer"
    on:mouseenter={() => handleHover(true)}
    on:mouseleave={() => handleHover(false)}
    on:click={handleClick}
    on:keydown={(e) => e.key === 'Enter' && handleClick()}
    tabindex="0"
    role="button"
    aria-label="Interactive growing plant"
  >
    <!-- Ground layers with texture -->
    <svg width="300" height="400" viewBox="0 0 300 400" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Ground hills and texture -->
      <g style="transform: translateY({mounted ? 0 : 20}px); opacity: {$groundMovement}; transition: transform 1s ease-out;">
        <!-- Dark soil base -->
        <path 
          d="M30 370 C30 370, 70 360, 90 365 C110 370, 130 375, 150 372 C170 370, 190 365, 210 367 C230 369, 250 375, 270 370 L280 390 L20 390 Z" 
          fill="#3E2723" 
          class="transition-all duration-500"
        />
        
        <!-- Middle soil layer -->
        <path 
          d="M35 370 C35 370, 70 {360 - $growthProgress * 5} 90 365 C110 {370 - $growthProgress * 4}, 130 375, 150 {372 - $growthProgress * 6} C170 {370 - $growthProgress * 3}, 190 365, 210 367 C230 {369 - $growthProgress * 5}, 250 375, 265 370" 
          fill="#5D4037" 
          class="transition-all duration-500"
        />
        
        <!-- Top soil layer with texture -->
        <path 
          d="M40 369 C40 369, 70 {359 - $growthProgress * 7} 90 364 C110 {368 - $growthProgress * 8}, 130 373, 150 {370 - $growthProgress * 10} C170 {368 - $growthProgress * 9}, 190 363, 210 365 C230 {367 - $growthProgress * 7}, 250 372, 260 369" 
          fill="#795548" 
          class="transition-all duration-500"
        />
        
        <!-- Soil texture details -->
        <g opacity="0.7">
          <path d="M60 365 L65 362" stroke="#8D6E63" stroke-width="1" />
          <path d="M90 363 L95 361" stroke="#8D6E63" stroke-width="1" />
          <path d="M120 367 L125 364" stroke="#8D6E63" stroke-width="1" />
          <path d="M180 365 L185 362" stroke="#8D6E63" stroke-width="1" />
          <path d="M210 366 L215 363" stroke="#8D6E63" stroke-width="1" />
          <path d="M240 368 L245 365" stroke="#8D6E63" stroke-width="1" />
        </g>
        
        <!-- Grass blades -->
        <g opacity="0.8" style="transform: translateY({-$growthProgress * 2}px);">
          <path d="M55 364 C55 364, 53 359, 54 356" stroke="#81C784" stroke-width="1" stroke-linecap="round" />
          <path d="M75 362 C75 362, 78 357, 76 354" stroke="#81C784" stroke-width="1" stroke-linecap="round" />
          <path d="M100 363 C100 363, 98 358, 99 355" stroke="#81C784" stroke-width="1" stroke-linecap="round" />
          <path d="M195 363 C195 363, 197 358, 196 355" stroke="#81C784" stroke-width="1" stroke-linecap="round" />
          <path d="M225 366 C225 366, 222 361, 223 358" stroke="#81C784" stroke-width="1" stroke-linecap="round" />
          <path d="M245 367 C245 367, 248 362, 247 359" stroke="#81C784" stroke-width="1" stroke-linecap="round" />
        </g>
      </g>
        
      {#if growthStage === 0}
        <!-- STAGE 0: SPROUT - Enhanced Realism with Emoji-Style Stem -->
        <g
        style="
        transform: translateY({mounted ? 0 : 20}px) scale(1, {$growthProgress}) 
                rotate({3 - $growthProgress * 3}deg);
        transform-origin: bottom center;
        opacity: {$growthProgress};
        transition: transform 1.5s ease-out;
        "
        class="transition-all duration-2000"
        >
        <!-- Create gradient definitions with fresher, brighter colors -->
        <defs>
        <linearGradient id="stemGradient0" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="10%" stop-color="#2E8B57" /> <!-- Darker emoji green for stem base -->
            <stop offset="50%" stop-color="#3CB371" /> <!-- Medium green for mid-stem -->
            <stop offset="90%" stop-color="#4CAF50" /> <!-- Light green at tip -->
        </linearGradient>
        <linearGradient id="leafGradient0" x1="0%" y1="100%" x2="100%" y2="0%">
            <stop offset="10%" stop-color="#66BB6A" /> <!-- Light-medium green -->
            <stop offset="50%" stop-color="#81C784" /> <!-- Light green mid-leaf -->
            <stop offset="90%" stop-color="#A5D6A7" /> <!-- Very light green highlight -->
        </linearGradient>
        <!-- Color transition for maturity -->
        <linearGradient id="matureLeafGradient" x1="0%" y1="100%" x2="100%" y2="0%">
            <stop offset="10%" stop-color={`hsl(${120 - $growthProgress * 10}, ${75 - $growthProgress * 15}%, ${45 + $growthProgress * 5}%)`} />
            <stop offset="50%" stop-color={`hsl(${120 - $growthProgress * 10}, ${75 - $growthProgress * 10}%, ${55 + $growthProgress * 5}%)`} />
            <stop offset="90%" stop-color={`hsl(${120 - $growthProgress * 10}, ${80 - $growthProgress * 15}%, ${65 + $growthProgress * 5}%)`} />
        </linearGradient>
        <!-- Fresh sprout glow -->
        <filter id="sproutGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="1.2" result="blur" />
            <feColorMatrix in="blur" type="matrix" values="0 0 0 0 0.4 0 0 0 0 0.8 0 0 0 0 0.4 0 0 0 0.6 0" result="glow" />
            <feComposite in="SourceGraphic" in2="glow" operator="over" />
        </filter>
        </defs>

        <!-- Soft glow behind stem - brighter and more vibrant -->
        <path
        d="M150 350 C149 345, 150 338, 150 325 C149 320, 150 318, 150 318"
        stroke="#A5D6A7"
        stroke-width="4"
        fill="none"
        opacity={0.6 * (1 - $growthProgress)}
        filter="url(#sproutGlow)"
        style="
            transform: rotate({calculateWindEffect(3, 0.3)}deg) skewX({calculateWindEffect(1, 0.3)}deg);
            transform-origin: bottom;
            transition: transform 1.8s ease-out;
        "
        />

        <!-- Emoji-style stem - smooth, simple curve -->
        <path
        d="M150 350 C149 345, 150 338, 150 325 C149 320, 150 318, 150 318"
        stroke="url(#stemGradient0)"
        stroke-width="3.5"
        stroke-linecap="round"
        fill="none"
        style="
            transform: rotate({calculateWindEffect(3, 0.3)}deg) 
                    skewX({calculateWindEffect(1, 0.3)}deg) 
                    scaleY({0.9 + $growthProgress * 0.1});
            transform-origin: bottom;
            transition: transform 1.8s ease-out;
        "
        />

        <!-- Morning dew effect at soil level -->
        <ellipse
        cx="150"
        cy="350"
        rx="5"
        ry="1.5"
        fill="rgba(73, 160, 120, 0.3)"
        style="transform: scaleX({1 + Math.sin(Date.now() / 2000) * 0.05});"
        />

        <!-- Micro trembling effect - very subtle random motion for young sprouts -->
        <g
        style="
            transform: translate(
            ${$growthProgress < 0.4 ? Math.sin(Date.now() / 300) * 0.3 : 0}px,
            ${$growthProgress < 0.4 ? Math.cos(Date.now() / 270) * 0.2 : 0}px
            );
        "
        class="transition-transform duration-100"
        >
        <!-- Left leaf - attached properly to stem with brighter colors -->
        <path
            d="M148 324 C143 322, 138 317, 140 312 C141 309, 139 308, 141 306 C144 305, 146 310, 148 312 C150 313, 149 317, 150 320 C149 322, 148 324, 148 324 Z"
            fill={$growthProgress > 0.6 ? "url(#matureLeafGradient)" : "url(#leafGradient0)"}
            stroke="#66BB6A"
            stroke-width="0.5"
            style="
            transform: rotate({$windStrength * 6 - 5 + Math.sin(Date.now() / 500) * 2}deg) 
                        scale({$leafUnfurl}, {$leafUnfurl}) 
                        rotateX({60 - $leafUnfurl * 60}deg);
            transform-origin: 148px 324px;
            opacity: {$leafUnfurl};
            transition: transform 1.2s ease-out, rotate 0.8s ease-out;
            "
            class="transition-all duration-800"
        />
        
        <!-- Right leaf - attached properly to stem with brighter colors -->
        <path
            d="M152 324 C157 320, 164 319, 162 312 C161 309, 164 307, 161 305 C159 306, 156 311, 152 315 C150 317, 151 320, 153 322 C152 323, 152 324, 152 324 Z"
            fill={$growthProgress > 0.6 ? "url(#matureLeafGradient)" : "url(#leafGradient0)"}
            stroke="#66BB6A"
            stroke-width="0.5"
            style="
            transform: rotate({$windStrength * 6 + 8 + Math.sin(Date.now() / 550) * 2}deg) 
                        scale({$leafUnfurl}, {$leafUnfurl}) 
                        rotateX({60 - $leafUnfurl * 60}deg);
            transform-origin: 152px 324px;
            opacity: {$leafUnfurl};
            transition: transform 1.2s ease-out, rotate 0.8s ease-out;
            "
            class="transition-all duration-1000"
        />
        
        <!-- Lighter leaf veins -->
        <path
            d="M146 321 C146 320, 145 318, 144 316 M145 320 C143 317, 143 315, 143 313"
            stroke="#A5D6A7"
            stroke-width="0.3"
            opacity="0.8"
            style="
            transform: rotate({$windStrength * 6 - 5}deg);
            transform-origin: 148px 324px;
            opacity: {$leafUnfurl * 0.8};
            transition: transform 1.2s ease-out;
            "
        />
        
        <path
            d="M154 320 C155 319, 156 317, 157 315 M153 321 C155 318, 158 316, 158 313"
            stroke="#A5D6A7"
            stroke-width="0.3"
            opacity="0.8"
            style="
            transform: rotate({$windStrength * 6 + 8}deg);
            transform-origin: 152px 324px;
            opacity: {$leafUnfurl * 0.8};
            transition: transform 1.2s ease-out;
            "
        />
        </g>

        <!-- Dynamic water droplet with sliding and pulsing -->
        <circle
        cx={151 + Math.sin($windStrength * 5) * 0.5}
        cy={315 + $growthProgress * 10} 
        r={0.8 + Math.sin(Date.now() / 1000) * 0.2}
        fill="rgba(255, 255, 255, 0.85)"
        style="
            opacity: {$growthProgress < 0.6 ? $growthProgress * 1.5 : (1 - $growthProgress) * 2.5};
            transition: cy 3s ease-out;
            filter: url(#sproutGlow);
        "
        />

        <!-- Smaller dewdrop at base of second leaf -->
        <circle
        cx={152 + Math.sin($windStrength * 3) * 0.3}
        cy="324"
        r={0.5 + Math.sin(Date.now() / 1200) * 0.1}
        fill="rgba(255, 255, 255, 0.7)"
        style="
            opacity: {$growthProgress < 0.7 ? $growthProgress * 1.3 : (1 - $growthProgress) * 3};
        "
        />
        </g>
        
      {:else if growthStage === 1}
        <!-- STAGE 1: ENHANCED YOUNG PLANT - More realistic stems and leaves -->
<g style="transform-origin: bottom;">
    <!-- Create enhanced gradient definitions -->
    <defs>
      <!-- Stem gradients with more color variation -->
      <linearGradient id="stemGradient1" x1="0%" y1="100%" x2="0%" y2="0%">
        <stop offset="0%" stop-color="#2E7D32" /> <!-- Dark base -->
        <stop offset="30%" stop-color="#388E3C" /> <!-- Mid stem -->
        <stop offset="70%" stop-color="#43A047" /> <!-- Upper stem -->
        <stop offset="100%" stop-color="#4CAF50" /> <!-- Tip -->
      </linearGradient>
      
      <!-- Leaf gradients with better color distribution -->
      <linearGradient id="leafGradient1" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#2E7D32" /> <!-- Darker edge -->
        <stop offset="30%" stop-color="#388E3C" /> <!-- Mid leaf darker -->
        <stop offset="70%" stop-color="#43A047" /> <!-- Mid leaf lighter -->
        <stop offset="100%" stop-color="#66BB6A" /> <!-- Lightest highlight -->
      </linearGradient>
      
      <!-- Special highlight gradient for leaf shine -->
      <linearGradient id="leafHighlight" x1="30%" y1="30%" x2="70%" y2="70%">
        <stop offset="0%" stop-color="rgba(255, 255, 255, 0)" />
        <stop offset="50%" stop-color="rgba(255, 255, 255, 0.15)" />
        <stop offset="100%" stop-color="rgba(255, 255, 255, 0)" />
      </linearGradient>
      
      <!-- Leaf vein gradient -->
      <linearGradient id="veinGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#2E7D32" /> <!-- Darker -->
        <stop offset="100%" stop-color="#388E3C" /> <!-- Lighter -->
      </linearGradient>
      
      <!-- Filters for enhanced realism -->
      <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur in="SourceAlpha" stdDeviation="1" />
        <feOffset dx="0.5" dy="0.5" />
        <feComponentTransfer>
          <feFuncA type="linear" slope="0.5" />
        </feComponentTransfer>
        <feMerge>
          <feMergeNode />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
      
      <filter id="dewdropGlow" x="-30%" y="-30%" width="160%" height="160%">
        <feGaussianBlur stdDeviation="0.5" result="blur" />
        <feColorMatrix in="blur" type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.6 0" result="glow" />
        <feComposite in="SourceGraphic" in2="glow" operator="over" />
      </filter>
    </defs>
    
    <!-- Main Stem with more naturalistic curve and thickness variation -->
    <path 
      d="M150 350 C149 335, 151 320, 149 305 C147 290, 152 275, 150 260" 
      stroke="url(#stemGradient1)" 
      stroke-width="4"
      stroke-linecap="round"
      fill="none"
      style="
        transform: rotate(calc({$windStrength} * 2deg)) skewX(calc({$windStrength} * 0.5deg)); 
        transform-origin: bottom;
        transform-box: fill-box;
        opacity: {$growthProgress};
        transition: transform 1.8s ease-out;
      "
    />
    
    <!-- Side Stems with naturalistic curves and thickness -->
    <!-- Right branch -->
    <path 
      d="M149 305 C156 302, 163 300, 170 296 C177 292, 183 287, 180 285" 
      stroke="url(#stemGradient1)" 
      stroke-width="2.5"
      stroke-linecap="round"
      fill="none"
      style="
        transform: rotate(calc({$windStrength} * 3deg + {Math.sin(Date.now() / 1200) * 1}deg)) scale(1, {0.3 + $growthProgress * 0.7}); 
        transform-origin: 149px 305px;
        opacity: {$growthProgress};
        transition: transform 1.5s ease-out;
      "
    />
    
    <!-- Left branch -->
    <path 
      d="M151 280 C144 278, 136 274, 128 272 C120 270, 115 267, 118 265" 
      stroke="url(#stemGradient1)" 
      stroke-width="2"
      stroke-linecap="round"
      fill="none"
      style="
        transform: rotate(calc({$windStrength} * 2.5deg + {Math.sin(Date.now() / 1300) * 1}deg)) scale(1, {0.3 + $growthProgress * 0.7}); 
        transform-origin: 151px 280px;
        opacity: {$growthProgress};
        transition: transform 1.6s ease-out;
      "
    />
    
    <!-- Enhanced realistic leaves -->
    <!-- Right leaf cluster -->
    <g style="
      transform-origin: 180px 285px;
      transform: rotate(calc({$windStrength} * 4deg + {Math.sin(Date.now() / 900) * 2}deg));
      opacity: {$leafUnfurl};
      transition: transform 1.4s ease-out;
    ">
      <!-- Main leaf body -->
      <path 
        d="M180 285 C187 282, 198 282, 208 288 C215 293, 218 302, 213 310 C208 316, 195 318, 185 312 C175 306, 175 296, 180 285 Z" 
        fill="url(#leafGradient1)"
        stroke="#2E7D32"
        stroke-width="0.6"
        filter="url(#softShadow)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 180px 285px;
          transition: all 0.8s ease-out;
        "
      />
      
      <!-- Leaf shine/highlight overlay -->
      <path 
        d="M180 285 C187 282, 198 282, 208 288 C215 293, 218 302, 213 310 C208 316, 195 318, 185 312 C175 306, 175 296, 180 285 Z" 
        fill="url(#leafHighlight)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 180px 285px;
          transition: all 0.8s ease-out;
        "
      />
      
      <!-- Realistic leaf veins -->
      <path 
        d="M180 285 C187 290, 195 296, 202 302" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 180px 285px;
          transition: all 0.8s ease-out;
        "
      />
      
      <path 
        d="M180 285 C190 292, 198 300, 205 306" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 180px 285px;
          transition: all 0.8s ease-out;
        "
      />
      
      <path 
        d="M180 285 C188 297, 194 305, 197 310" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 180px 285px;
          transition: all 0.8s ease-out;
        "
      />
      
      <!-- Dewdrop on leaf -->
      <circle
        cx="195"
        cy="295"
        r="{1 + Math.sin(Date.now() / 1000) * 0.2}"
        fill="rgba(255, 255, 255, 0.85)"
        filter="url(#dewdropGlow)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 180px 285px;
          opacity: {$growthProgress < 0.8 ? $leafUnfurl * 0.9 : (1 - $growthProgress) * 4.5};
          transition: all 0.8s ease-out;
        "
      />
    </g>
    
    <!-- Left leaf cluster -->
    <g style="
      transform-origin: 118px 265px;
      transform: rotate(calc({$windStrength} * -3deg + {Math.sin(Date.now() / 950) * 2}deg));
      opacity: {$leafUnfurl};
      transition: transform 1.4s ease-out;
    ">
      <!-- Main leaf body -->
      <path 
        d="M118 265 C112 262, 101 262, 92 268 C85 273, 82 282, 87 290 C92 296, 105 298, 115 292 C125 286, 123 275, 118 265 Z" 
        fill="url(#leafGradient1)"
        stroke="#2E7D32"
        stroke-width="0.6"
        filter="url(#softShadow)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 118px 265px;
          transition: all 0.9s ease-out;
        "
      />
      
      <!-- Leaf shine/highlight overlay -->
      <path 
        d="M118 265 C112 262, 101 262, 92 268 C85 273, 82 282, 87 290 C92 296, 105 298, 115 292 C125 286, 123 275, 118 265 Z" 
        fill="url(#leafHighlight)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 118px 265px;
          transition: all 0.9s ease-out;
        "
      />
      
      <!-- Realistic leaf veins -->
      <path 
        d="M118 265 C112 271, 105 277, 98 283" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 118px 265px;
          transition: all 0.9s ease-out;
        "
      />
      
      <path 
        d="M118 265 C108 273, 100 282, 93 287" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 118px 265px;
          transition: all 0.9s ease-out;
        "
      />
      
      <path 
        d="M118 265 C113 277, 104 285, 96 290" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 118px 265px;
          transition: all 0.9s ease-out;
        "
      />
    </g>
    
    <!-- Top leaves -->
    <g style="
      transform-origin: 150px 260px;
      transform: rotate(calc({$windStrength} * 2.5deg + {Math.sin(Date.now() / 800) * 1.5}deg));
      opacity: {$leafUnfurl};
      transition: transform 1.2s ease-out;
    ">
      <!-- Right top leaf -->
      <path 
        d="M150 260 C155 255, 163 252, 170 255 C177 258, 180 267, 175 273 C170 277, 160 275, 155 270 C150 265, 148 262, 150 260 Z" 
        fill="url(#leafGradient1)"
        stroke="#2E7D32"
        stroke-width="0.6"
        filter="url(#softShadow)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          transition: all 1s ease-out;
        "
      />
      
      <!-- Right top leaf highlight -->
      <path 
        d="M150 260 C155 255, 163 252, 170 255 C177 258, 180 267, 175 273 C170 277, 160 275, 155 270 C150 265, 148 262, 150 260 Z" 
        fill="url(#leafHighlight)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          transition: all 1s ease-out;
        "
      />
      
      <!-- Right leaf veins -->
      <path 
        d="M150 260 C158 262, 165 265, 170 270" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          transition: all 1s ease-out;
        "
      />
      
      <!-- Left top leaf -->
      <path 
        d="M150 260 C145 255, 137 252, 130 255 C123 258, 120 267, 125 273 C130 277, 140 275, 145 270 C150 265, 152 262, 150 260 Z" 
        fill="url(#leafGradient1)"
        stroke="#2E7D32"
        stroke-width="0.6"
        filter="url(#softShadow)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          transition: all 1s ease-out;
        "
      />
      
      <!-- Left top leaf highlight -->
      <path 
        d="M150 260 C145 255, 137 252, 130 255 C123 258, 120 267, 125 273 C130 277, 140 275, 145 270 C150 265, 152 262, 150 260 Z" 
        fill="url(#leafHighlight)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          transition: all 1s ease-out;
        "
      />
      
      <!-- Left leaf veins -->
      <path 
        d="M150 260 C142 262, 135 265, 130 270" 
        stroke="url(#veinGradient)" 
        stroke-width="0.5"
        opacity="0.7"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          transition: all 1s ease-out;
        "
      />
      
      <!-- Top dewdrop -->
      <circle
        cx="150"
        cy="260"
        r="{0.8 + Math.sin(Date.now() / 1100) * 0.15}"
        fill="rgba(255, 255, 255, 0.9)"
        filter="url(#dewdropGlow)"
        style="
          transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
          transform-origin: 150px 260px;
          opacity: {$growthProgress < 0.8 ? $leafUnfurl * 0.9 : (1 - $growthProgress) * 4.5};
          transition: all 1s ease-out;
        "
      />
    </g>
    
    <!-- Small environment details -->
    <!-- Soil moisture -->
    <ellipse
      cx="150"
      cy="350"
      rx="8"
      ry="2"
      fill="rgba(62, 39, 35, 0.5)"
      style="
        transform: scaleX({1 + Math.sin(Date.now() / 2000) * 0.05});
        opacity: {0.6 * $growthProgress};
        filter: url(#softShadow);
      "
    />
    
    <!-- Stem shadow on soil -->
    <ellipse
      cx="150"
      cy="350"
      rx="3"
      ry="0.8"
      fill="rgba(30, 60, 40, 0.3)"
      style="
        transform: translateX({$windStrength * 1}px);
        opacity: {0.5 * $growthProgress};
      "
    />
    
    <!-- Subtle ambient movement for all stems and leaves -->
    <animate
      attributeName="opacity"
      from="{$growthProgress}"
      to="{$growthProgress}"
      dur="10s"
      repeatCount="indefinite"
      calcMode="spline"
      keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"
    />
  </g>
      {:else if growthStage === 2}
        <!-- STAGE 2: SMALL TREE WITH ORGANIC SHAPES -->
        <!-- STAGE 7: MATURE PLANT - With additional foliage, buds and early flowering -->
<g style="transform-origin: bottom;">
  <!-- Enhanced gradient definitions -->
  <defs>
    <!-- Stem gradients with mature plant coloration -->
    <linearGradient id="matureStemGradient" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#1B5E20" /> <!-- Darker base for mature stem -->
      <stop offset="40%" stop-color="#2E7D32" /> <!-- Mid stem -->
      <stop offset="80%" stop-color="#388E3C" /> <!-- Upper stem -->
      <stop offset="100%" stop-color="#43A047" /> <!-- Tip -->
    </linearGradient>
    
    <!-- Mature leaf gradient with deeper, richer coloring -->
    <linearGradient id="matureLeafGradient" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1B5E20" /> <!-- Darker edge for mature leaf -->
      <stop offset="40%" stop-color="#2E7D32" /> <!-- Mid leaf darker -->
      <stop offset="70%" stop-color="#388E3C" /> <!-- Mid leaf lighter -->
      <stop offset="100%" stop-color="#43A047" /> <!-- Highlight area -->
    </linearGradient>
    
    <!-- Young leaf gradient (for new growth) -->
    <linearGradient id="youngLeafGradient" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2E7D32" /> <!-- Slightly lighter base -->
      <stop offset="40%" stop-color="#388E3C" /> <!-- Mid leaf -->
      <stop offset="70%" stop-color="#43A047" /> <!-- Mid leaf lighter -->
      <stop offset="100%" stop-color="#66BB6A" /> <!-- Brightest highlight -->
    </linearGradient>
    
    <!-- Bud/flower gradients -->
    <linearGradient id="budGradient" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#388E3C" /> <!-- Base -->
      <stop offset="60%" stop-color="#4CAF50" /> <!-- Mid -->
      <stop offset="100%" stop-color="#66BB6A" /> <!-- Tip -->
    </linearGradient>
    
    <linearGradient id="flowerGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5F5F5" /> <!-- White flower base -->
      <stop offset="50%" stop-color="#FFFFFF" /> <!-- Pure white -->
      <stop offset="100%" stop-color="#E0F7FA" /> <!-- Slight blue tint -->
    </linearGradient>
    
    <linearGradient id="flowerCenterGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF176" /> <!-- Light yellow -->
      <stop offset="100%" stop-color="#FFD54F" /> <!-- Darker yellow -->
    </linearGradient>
    
    <!-- Special highlight gradient for leaf shine -->
    <linearGradient id="leafHighlight" x1="30%" y1="30%" x2="70%" y2="70%">
      <stop offset="0%" stop-color="rgba(255, 255, 255, 0)" />
      <stop offset="50%" stop-color="rgba(255, 255, 255, 0.12)" />
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0)" />
    </linearGradient>
    
    <!-- Vein gradient -->
    <linearGradient id="veinGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1B5E20" /> <!-- Darker -->
      <stop offset="100%" stop-color="#2E7D32" /> <!-- Lighter -->
    </linearGradient>
    
    <!-- Enhanced filters -->
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="1" />
      <feOffset dx="0.5" dy="0.5" />
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.5" />
      </feComponentTransfer>
      <feMerge>
        <feMergeNode />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    
    <filter id="dewdropGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="0.5" result="blur" />
      <feColorMatrix in="blur" type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.6 0" result="glow" />
      <feComposite in="SourceGraphic" in2="glow" operator="over" />
    </filter>
    
    <filter id="flowerGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="1" result="blur" />
      <feColorMatrix in="blur" type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.3 0" result="glow" />
      <feComposite in="SourceGraphic" in2="glow" operator="over" />
    </filter>
  </defs>
  
  <!-- Main mature stem with more complex structure -->
  <path 
    d="M150 350 C148 330, 151 310, 147 290 C143 270, 153 250, 149 230 C145 210, 152 190, 150 170" 
    stroke="url(#matureStemGradient)" 
    stroke-width="5"
    stroke-linecap="round"
    fill="none"
    style="
      transform: rotate(calc({$windStrength} * 1.5deg)) skewX(calc({$windStrength} * 0.3deg)); 
      transform-origin: bottom;
      transform-box: fill-box;
      opacity: {$growthProgress};
      transition: transform 2.5s ease-out;
    "
  />
  
  <!-- Multiple side branches -->
  <!-- Branch 1 (lower right) -->
  <path 
    d="M147 290 C155 288, 165 285, 175 278 C185 271, 195 260, 193 255" 
    stroke="url(#matureStemGradient)" 
    stroke-width="3"
    stroke-linecap="round"
    fill="none"
    style="
      transform: rotate(calc({$windStrength} * 2.5deg + {Math.sin(Date.now() / 1400) * 1}deg));
      transform-origin: 147px 290px;
      opacity: {$growthProgress};
      transition: transform 2.2s ease-out;
    "
  />
  
  <!-- Branch 2 (middle left) -->
  <path 
    d="M149 230 C140 228, 130 225, 118 220 C106 215, 95 208, 100 205" 
    stroke="url(#matureStemGradient)" 
    stroke-width="2.5"
    stroke-linecap="round"
    fill="none"
    style="
      transform: rotate(calc({$windStrength} * 2deg + {Math.sin(Date.now() / 1300) * 1.2}deg));
      transform-origin: 149px 230px;
      opacity: {$growthProgress};
      transition: transform 2.3s ease-out;
    "
  />
  
  <!-- Branch 3 (upper right) -->
  <path 
    d="M150 170 C158 168, 168 165, 178 160 C188 155, 195 145, 190 140" 
    stroke="url(#matureStemGradient)" 
    stroke-width="2"
    stroke-linecap="round"
    fill="none"
    style="
      transform: rotate(calc({$windStrength} * 3deg + {Math.sin(Date.now() / 1200) * 1.5}deg));
      transform-origin: 150px 170px;
      opacity: {$growthProgress};
      transition: transform 2s ease-out;
    "
  />
  
  <!-- Sub-branch from Branch 1 -->
  <path 
    d="M175 278 C180 270, 182 262, 185 255" 
    stroke="url(#matureStemGradient)" 
    stroke-width="1.5"
    stroke-linecap="round"
    fill="none"
    style="
      transform: rotate(calc({$windStrength} * 3.5deg + {Math.sin(Date.now() / 1100) * 1.5}deg));
      transform-origin: 175px 278px;
      opacity: {$growthProgress * 0.9};
      transition: transform 1.8s ease-out;
    "
  />
  
  <!-- Lower mature leaves -->
  <!-- Mature leaf on Branch 1 -->
  <g style="
    transform-origin: 193px 255px;
    transform: rotate(calc({$windStrength} * 4deg + {Math.sin(Date.now() / 950) * 2.5}deg));
    opacity: {$leafUnfurl};
    transition: transform 1.9s ease-out;
  ">
    <!-- Main leaf body -->
    <path 
      d="M193 255 C200 250, 215 248, 230 255 C240 262, 245 275, 235 285 C225 295, 205 298, 190 290 C175 282, 183 265, 193 255 Z" 
      fill="url(#matureLeafGradient)"
      stroke="#1B5E20"
      stroke-width="0.7"
      filter="url(#softShadow)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 193px 255px;
        transition: all 1.8s ease-out;
      "
    />
    
    <!-- Leaf highlight -->
    <path 
      d="M193 255 C200 250, 215 248, 230 255 C240 262, 245 275, 235 285 C225 295, 205 298, 190 290 C175 282, 183 265, 193 255 Z" 
      fill="url(#leafHighlight)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 193px 255px;
        transition: all 1.8s ease-out;
      "
    />
    
    <!-- Primary vein -->
    <path 
      d="M193 255 C205 260, 217 268, 228 275" 
      stroke="url(#veinGradient)" 
      stroke-width="0.8"
      opacity="0.8"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 193px 255px;
        transition: all 1.8s ease-out;
      "
    />
    
    <!-- Secondary veins -->
    <path 
      d="M205 260 C210 265, 215 270, 220 272 M215 268 C222 270, 228 272, 232 274 M225 275 C230 278, 234 282, 238 284" 
      stroke="url(#veinGradient)" 
      stroke-width="0.4"
      opacity="0.7"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 193px 255px;
        transition: all 1.8s ease-out;
      "
    />
  </g>
  
  <!-- Mature leaf on Branch 2 (left) -->
  <g style="
    transform-origin: 100px 205px;
    transform: rotate(calc({$windStrength} * -3.5deg + {Math.sin(Date.now() / 1050) * 2}deg));
    opacity: {$leafUnfurl};
    transition: transform 2.1s ease-out;
  ">
    <!-- Main leaf body -->
    <path 
      d="M100 205 C93 200, 78 198, 63 205 C53 212, 48 225, 58 235 C68 245, 88 248, 103 240 C118 232, 110 215, 100 205 Z" 
      fill="url(#matureLeafGradient)"
      stroke="#1B5E20"
      stroke-width="0.7"
      filter="url(#softShadow)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 100px 205px;
        transition: all 2s ease-out;
      "
    />
    
    <!-- Leaf highlight -->
    <path 
      d="M100 205 C93 200, 78 198, 63 205 C53 212, 48 225, 58 235 C68 245, 88 248, 103 240 C118 232, 110 215, 100 205 Z" 
      fill="url(#leafHighlight)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 100px 205px;
        transition: all 2s ease-out;
      "
    />
    
    <!-- Primary vein -->
    <path 
      d="M100 205 C88 210, 76 218, 65 225" 
      stroke="url(#veinGradient)" 
      stroke-width="0.8"
      opacity="0.8"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 100px 205px;
        transition: all 2s ease-out;
      "
    />
    
    <!-- Secondary veins -->
    <path 
      d="M88 210 C83 215, 78 220, 73 222 M78 218 C73 220, 67 222, 63 224 M68 225 C65 228, 60 232, 56 234" 
      stroke="url(#veinGradient)" 
      stroke-width="0.4"
      opacity="0.7"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 100px 205px;
        transition: all 2s ease-out;
      "
    />
  </g>
  
  <!-- Newer growth leaves (lighter green) -->
  <!-- Young leaf on Branch 3 -->
  <g style="
    transform-origin: 190px 140px;
    transform: rotate(calc({$windStrength} * 4.5deg + {Math.sin(Date.now() / 900) * 3}deg));
    opacity: {$leafUnfurl * 0.9};
    transition: transform 1.7s ease-out;
  ">
    <!-- Main leaf body -->
    <path 
      d="M190 140 C195 135, 205 132, 215 135 C225 138, 230 150, 225 158 C220 166, 205 167, 195 162 C185 157, 182 147, 190 140 Z" 
      fill="url(#youngLeafGradient)"
      stroke="#2E7D32"
      stroke-width="0.6"
      filter="url(#softShadow)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8}) 
                   rotateX({10 - $leafUnfurl * 10}deg);
        transform-origin: 190px 140px;
        transition: all 1.7s ease-out;
      "
    />
    
    <!-- Leaf highlight -->
    <path 
      d="M190 140 C195 135, 205 132, 215 135 C225 138, 230 150, 225 158 C220 166, 205 167, 195 162 C185 157, 182 147, 190 140 Z" 
      fill="url(#leafHighlight)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8})
                   rotateX({10 - $leafUnfurl * 10}deg);
        transform-origin: 190px 140px;
        transition: all 1.7s ease-out;
      "
    />
    
    <!-- Primary vein -->
    <path 
      d="M190 140 C200 145, 210 153, 218 158" 
      stroke="url(#veinGradient)" 
      stroke-width="0.6"
      opacity="0.7"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 190px 140px;
        transition: all 1.7s ease-out;
      "
    />
    
    <!-- Dewdrop on young leaf -->
    <circle
      cx="205"
      cy="145"
      r="{0.9 + Math.sin(Date.now() / 900) * 0.2}"
      fill="rgba(255, 255, 255, 0.9)"
      filter="url(#dewdropGlow)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 190px 140px;
        opacity: {$leafUnfurl * 0.9};
        transition: all 1.7s ease-out;
      "
    />
  </g>
  
  <!-- Young leaf on sub-branch -->
  <g style="
    transform-origin: 185px 255px;
    transform: rotate(calc({$windStrength} * 5deg + {Math.sin(Date.now() / 850) * 3.5}deg));
    opacity: {$leafUnfurl * 0.95};
    transition: transform 1.5s ease-out;
  ">
    <!-- Main leaf body -->
    <path 
      d="M185 255 C190 250, 198 247, 205 250 C212 253, 215 260, 210 265 C205 270, 195 273, 187 268 C179 263, 180 258, 185 255 Z" 
      fill="url(#youngLeafGradient)"
      stroke="#2E7D32"
      stroke-width="0.5"
      filter="url(#softShadow)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8})
                   rotateX({15 - $leafUnfurl * 15}deg);
        transform-origin: 185px 255px;
        transition: all 1.5s ease-out;
      "
    />
    
    <!-- Leaf highlight -->
    <path 
      d="M185 255 C190 250, 198 247, 205 250 C212 253, 215 260, 210 265 C205 270, 195 273, 187 268 C179 263, 180 258, 185 255 Z" 
      fill="url(#leafHighlight)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8})
                   rotateX({15 - $leafUnfurl * 15}deg);
        transform-origin: 185px 255px;
        transition: all 1.5s ease-out;
      "
    />
    
    <!-- Veins -->
    <path 
      d="M185 255 C192 258, 198 262, 205 265" 
      stroke="url(#veinGradient)" 
      stroke-width="0.4"
      opacity="0.7"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8});
        transform-origin: 185px 255px;
        transition: all 1.5s ease-out;
      "
    />
  </g>
  
  <!-- Top leaves/growth with opening bud/early flower -->
  <!-- Left top leaf -->
  <g style="
    transform-origin: 150px 170px;
    transform: rotate(calc({$windStrength} * -2deg + {Math.sin(Date.now() / 800) * 2}deg));
    opacity: {$leafUnfurl * 0.98};
    transition: transform 1.3s ease-out;
  ">
    <path 
      d="M150 170 C145 165, 135 162, 128 166 C121 170, 118 180, 123 185 C128 190, 138 188, 145 183 C152 178, 153 173, 150 170 Z" 
      fill="url(#youngLeafGradient)"
      stroke="#2E7D32"
      stroke-width="0.5"
      filter="url(#softShadow)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8})
                   rotateX({5 - $leafUnfurl * 5}deg);
        transform-origin: 150px 170px;
        transition: all 1.3s ease-out;
      "
    />
    
    <path 
      d="M150 170 C145 165, 135 162, 128 166 C121 170, 118 180, 123 185 C128 190, 138 188, 145 183 C152 178, 153 173, 150 170 Z" 
      fill="url(#leafHighlight)"
      style="
        transform: scale({0.2 + $leafUnfurl * 0.8}, {0.2 + $leafUnfurl * 0.8})
                   rotateX({5 - $leafUnfurl * 5}deg);
        transform-origin: 150px 170px;
        transition: all 1.3s ease-out;
      "
    />
  </g>
  
  <!-- Bud/early flower at top -->
  <g style="
    transform-origin: 150px 170px; 
    transform: rotate(calc({$windStrength} * 1deg + {Math.sin(Date.now() / 1000) * 1}deg));
    opacity: {$leafUnfurl * 0.95};
    transition: transform 1.5s ease-out;
  ">
    <!-- Bud base -->
    <path 
      d="M150 170 C153 165, 152 160, 150 155 C148 153, 146 152, 145 152 C143 152, 141 153, 140 155 C138 158, 138 162, 140 165 C142 168, 147 170, 150 170 Z"
      fill="url(#budGradient)"
      stroke="#2E7D32"
      stroke-width="0.4"
      filter="url(#softShadow)"
      style="
        transform-origin: 150px 170px;
        transition: all 1.5s ease-out;
      "
    />
    
    <!-- Flower/bud opening animation -->
    <g style="
      transform-origin: 145px 155px;
      transform: scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7})
                 rotate({360 * $leafUnfurl * 0.2}deg);
      opacity: {$leafUnfurl * 0.9};
      transition: all 2s ease-out;
    ">
      <!-- Flower petals -->
      <path 
        d="M145 155 C148 152, 152 150, 155 152 C158 154, 160 158, 158 161 C156 164, 152 165, 149 163 C146 161, 144 158, 145 155 Z" 
        fill="url(#flowerGradient)"
        stroke="#E0F7FA"
        stroke-width="0.3"
        filter="url(#flowerGlow)"
        style="
          transform: rotate(0deg);
          transform-origin: 145px 155px;
          opacity: {$leafUnfurl * 0.9};
        "
      />
      
      <path 
        d="M145 155 C142 152, 138 150, 135 152 C132 154, 130 158, 132 161 C134 164, 138 165, 141 163 C144 161, 146 158, 145 155 Z" 
        fill="url(#flowerGradient)"
        stroke="#E0F7FA"
        stroke-width="0.3"
        filter="url(#flowerGlow)"
        style="
          transform: rotate(72deg);
          transform-origin: 145px 155px;
          opacity: {$leafUnfurl * 0.85};
        "
      />
      
      <path 
        d="M145 155 C143 151, 142 146, 144 143 C146 140, 150 138, 153 140 C156 142, 157 146, 155 149 C153 152, 148 153, 145 155 Z" 
        fill="url(#flowerGradient)"
        stroke="#E0F7FA"
        stroke-width="0.3"
        filter="url(#flowerGlow)"
        style="
          transform: rotate(144deg);
          transform-origin: 145px 155px;
          opacity: {$leafUnfurl * 0.8};
        "
      />
      
      <path 
        d="M145 155 C143 159, 142 164, 144 167 C146 170, 150 172, 153 170 C156 168, 157 164, 155 161 C153 158, 148 157, 145 155 Z" 
        fill="url(#flowerGradient)"
        stroke="#E0F7FA"
        stroke-width="0.3"
        filter="url(#flowerGlow)"
        style="
          transform: rotate(216deg);
          transform-origin: 145px 155px;
          opacity: {$leafUnfurl * 0.75};
        "
      />
      
      <path 
        d="M145 155 C147 159, 148 164, 146 167 C144 170, 140 172, 137 170 C134 168, 133 164, 135 161 C137 158, 142 157, 145 155 Z" 
        fill="url(#flowerGradient)"
        stroke="#E0F7FA"
        stroke-width="0.3"
        filter="url(#flowerGlow)"
        style="
          transform: rotate(288deg);
          transform-origin: 145px 155px;
          opacity: {$leafUnfurl * 0.7};
        "
      />
      
      <!-- Flower center -->
      <circle
        cx="145"
        cy="155"
        r="2.5"
        fill="url(#flowerCenterGradient)"
        stroke="#FFD54F"
        stroke-width="0.2"
        filter="url(#flowerGlow)"
        style="
          opacity: {$leafUnfurl * 0.95};
          transform-origin: 145px 155px;
        "
      />
    </g>
  </g>
  
  <!-- Environmental effects -->
  <!-- Soil moisture area -->
  <ellipse
    cx="150"
    cy="350"
    rx="12"
    ry="3"
    fill="rgba(62, 39, 35, 0.6)"
    style="
      transform: scaleX({1 + Math.sin(Date.now() / 2200) * 0.05});
      opacity: {0.7 * $growthProgress};
      filter: url(#softShadow);
    "
  />
  
  <!-- Plant shadow on soil -->
  <ellipse
    cx="150"
    cy="350"
    rx="8"
    ry="2"
    fill="rgba(30, 60, 40, 0.35)"
    style="
      transform: translateX({$windStrength * 3}px);
      opacity: {0.6 * $growthProgress};
    "
  />
  
  <!-- Subtle dewdrop near soil -->
  <circle
    cx="155"
    cy="345"
    r="{1 + Math.sin(Date.now() / 1500) * 0.2}"
    fill="rgba(255, 255, 255, 0.7)"
    filter="url(#dewdropGlow)"
    style="
      opacity: {$growthProgress * 0.5};
    "
  />
  
  <!-- Ambient animations -->
  <animate
    attributeName="opacity"
    from="{$growthProgress}"
    to="{$growthProgress}"
    dur="12s"
    repeatCount="indefinite"
    calcMode="spline"
    keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"
  />
</g>
{:else if growthStage === 3}
<!-- STAGE 3: FULL MATURE TREE WITH REALISTIC DETAILS -->
<g style="transform-origin: bottom; opacity: {$growthProgress};">
<!-- Create gradient definitions -->
<defs>
  <linearGradient id="stemGradient3" x1="0%" y1="100%" x2="0%" y2="0%">
    <stop offset="0%" stop-color={stemBaseColor} />
    <stop offset="100%" stop-color={stemTipColor} />
  </linearGradient>
  
  <linearGradient id="leafGradient3" x1="20%" y1="80%" x2="80%" y2="20%">
    <stop offset="0%" stop-color={leafDarkColor} />
    <stop offset="100%" stop-color={leafLightColor} />
  </linearGradient>
  
  <radialGradient id="foliageGradient3" cx="50%" cy="50%" r="50%">
    <stop offset="20%" stop-color={leafLightColor} />
    <stop offset="100%" stop-color={leafDarkColor} />
  </radialGradient>
  
  <linearGradient id="fruitGradient3" x1="30%" y1="30%" x2="70%" y2="70%">
    <stop offset="0%" stop-color={fruitHighlightColor} />
    <stop offset="100%" stop-color={fruitColor} />
  </linearGradient>
  
  <filter id="shadowFilter" x="-20%" y="-20%" width="140%" height="140%">
    <feDropShadow dx="1" dy="1" stdDeviation="1" flood-opacity="0.3" />
  </filter>
</defs>

<!-- Main Trunk - natural, textured -->
<g style="transform: rotate({calculateWindEffect(0.5, 80)}deg) skewX({calculateWindEffect(0.3, 80)}deg); transform-origin: bottom;">
  <path 
    d="M150 350 C152 320, 149 290, 153 260 C157 230, 148 200, 150 190" 
    stroke="url(#stemGradient3)" 
    stroke-width="12"
    fill="none"
  />
  
  <!-- Trunk texture/bark details -->
  <path d="M145 330 L150 332" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
  <path d="M155 310 L152 308" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
  <path d="M147 290 L152 288" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
  <path d="M154 270 L149 268" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
  <path d="M151 250 L154 248" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
  <path d="M146 230 L152 228" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
  <path d="M153 210 L148 208" stroke={stemBaseColor} stroke-width="1" opacity="0.7" />
</g>

<!-- Large branches - curved and organic -->
<path 
  d="M150 300 C160 295, 175 292, 195 290 C215 288, 225 284, 210 280" 
  stroke="url(#stemGradient3)" 
  stroke-width="6"
  fill="none"
  style="
    transform: rotate({calculateWindEffect(1, 80)}deg) scale({0.4 + $growthProgress * 0.6}, {0.4 + $growthProgress * 0.6}); 
    transform-origin: 150px 300px;
  "
/>

<path 
  d="M150 270 C140 265, 125 262, 105 260 C85 258, 75 254, 90 250" 
  stroke="url(#stemGradient3)" 
  stroke-width="6"
  fill="none"
  style="
    transform: rotate({calculateWindEffect(1.2, 110)}deg) scale({0.4 + $growthProgress * 0.6}, {0.4 + $growthProgress * 0.6}); 
    transform-origin: 150px 270px;
  "
/>

<path 
  d="M150 230 C160 225, 170 215, 180 205 C190 195, 195 185, 190 190" 
  stroke="url(#stemGradient3)" 
  stroke-width="5"
  fill="none"
  style="
    transform: rotate({calculateWindEffect(1.5, 150)}deg) scale({0.4 + $growthProgress * 0.6}, {0.4 + $growthProgress * 0.6}); 
    transform-origin: 150px 230px;
  "
/>

<path 
  d="M150 210 C140 205, 130 195, 120 185 C110 175, 105 165, 110 170" 
  stroke="url(#stemGradient3)" 
  stroke-width="5"
  fill="none"
  style="
    transform: rotate({calculateWindEffect(1.4, 160)}deg) scale({0.4 + $growthProgress * 0.6}, {0.4 + $growthProgress * 0.6}); 
    transform-origin: 150px 210px;
  "
/>

<!-- Small branches with curves -->
<path 
  d="M210 280 C215 275, 220 272, 228 267 C236 262, 242 258, 235 260" 
  stroke="url(#stemGradient3)" 
  stroke-width="3"
  fill="none"
  style="
    transform: rotate({calculateWindEffect(2.5, 100)}deg) scale({0.4 + $growthProgress * 0.6}, {0.4 + $growthProgress * 0.6}); 
    transform-origin: 210px 280px;
  "
/>

<path 
  d="M90 250 C85 245, 80 242, 72 237 C64 232, 58 228, 65 230" 
  stroke="url(#stemGradient3)" 
  stroke-width="3"
  fill="none"
  style="
    transform: rotate({calculateWindEffect(2.7, 130)}deg) scale({0.4 + $growthProgress * 0.6}, {0.4 + $growthProgress * 0.6}); 
    transform-origin: 90px 250px;
  "
/>

<!-- Organic foliage shapes -->
<!-- Right large cluster -->
<path
  d="M235 260 C248 250, 260 255, 265 270 C270 285, 260 300, 245 305 
     C230 310, 215 305, 210 290 C205 275, 215 255, 235 260 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="1"
  style="
    transform: rotate({calculateWindEffect(3, 120)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 235px 260px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-800"
/>

<!-- Sub-cluster for density -->
<path
  d="M215 250 C225 240, 235 245, 240 255 C245 265, 240 275, 230 280 
     C220 285, 210 275, 210 265 C210 255, 210 245, 215 250 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="0.8"
  style="
    transform: rotate({calculateWindEffect(2.7, 130)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 215px 250px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-850"
/>

<!-- Left large cluster -->
<path
  d="M65 230 C52 220, 40 225, 35 240 C30 255, 40 270, 55 275 
     C70 280, 85 275, 90 260 C95 245, 85 225, 65 230 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="1"
  style="
    transform: rotate({calculateWindEffect(3.2, 150)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 65px 230px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-900"
/>

<!-- Sub-cluster for density -->
<path
  d="M85 220 C95 210, 105 215, 110 225 C115 235, 110 245, 100 250 
     C90 255, 80 245, 80 235 C80 225, 80 215, 85 220 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="0.8"
  style="
    transform: rotate({calculateWindEffect(2.9, 160)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 85px 220px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-950"
/>

<!-- Upper right cluster -->
<path
  d="M190 190 C200 180, 215 180, 225 190 C235 200, 235 215, 225 225 
     C215 235, 195 235, 185 225 C175 215, 175 195, 190 190 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="1"
  style="
    transform: rotate({calculateWindEffect(3.5, 190)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 190px 190px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-1000"
/>

<!-- Upper left cluster -->
<path
  d="M110 170 C100 160, 85 160, 75 170 C65 180, 65 195, 75 205 
     C85 215, 105 215, 115 205 C125 195, 125 175, 110 170 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="1"
  style="
    transform: rotate({calculateWindEffect(3.4, 210)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 110px 170px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-1050"
/>

<!-- Top cluster -->
<path
  d="M150 150 C160 140, 175 135, 185 145 C195 155, 195 170, 185 180 
     C175 190, 155 185, 145 175 C135 165, 135 150, 150 150 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="1"
  style="
    transform: rotate({calculateWindEffect(3, 230)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 150px 150px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-1100"
/>

<path
  d="M150 150 C140 140, 125 135, 115 145 C105 155, 105 170, 115 180 
     C125 190, 145 185, 155 175 C165 165, 165 150, 150 150 Z"
  fill="url(#foliageGradient3)"
  stroke={leafDarkColor}
  stroke-width="1"
  style="
    transform: rotate({calculateWindEffect(2.8, 230)}deg) scale({0.3 + $leafUnfurl * 0.7}, {0.3 + $leafUnfurl * 0.7});
    transform-origin: 150px 150px;
    opacity: {$leafUnfurl};
    filter: url(#shadowFilter);
  "
  class="transition-all duration-1150"
/>

<!-- Leaf vein details scattered throughout clusters -->
<g opacity={$leafUnfurl * 0.5} style="pointer-events: none;">
  <path d="M235 260 C240 265, 245 270, 250 275" stroke={leafDarkColor} stroke-width="0.4" />
  <path d="M65 230 C60 235, 55 240, 50 245" stroke={leafDarkColor} stroke-width="0.4" />
  <path d="M190 190 C195 195, 200 200, 205 205" stroke={leafDarkColor} stroke-width="0.4" />
  <path d="M110 170 C105 175, 100 180, 95 185" stroke={leafDarkColor} stroke-width="0.4" />
  <path d="M150 150 C155 155, 160 160, 165 165" stroke={leafDarkColor} stroke-width="0.4" />
  <path d="M150 150 C145 155, 140 160, 135 165" stroke={leafDarkColor} stroke-width="0.4" />
</g>

<!-- Detailed fruits -->
<!-- Right side fruits -->
<g style="filter: url(#shadowFilter);">
  <circle 
    cx="235" cy="265" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(3, 120)}px, {calculateWindEffect(2, 120)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="235" cy="265" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(3, 120) - 2}px, {calculateWindEffect(2, 120) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
  
  <circle 
    cx="210" cy="245" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(2.5, 130)}px, {calculateWindEffect(2, 130)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="210" cy="245" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(2.5, 130) - 2}px, {calculateWindEffect(2, 130) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
  
  <!-- Left side fruits -->
  <circle 
    cx="70" cy="235" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(2.8, 150)}px, {calculateWindEffect(2.2, 150)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="70" cy="235" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(2.8, 150) - 2}px, {calculateWindEffect(2.2, 150) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
  
  <circle 
    cx="95" cy="215" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(2.3, 170)}px, {calculateWindEffect(1.8, 170)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="95" cy="215" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(2.3, 170) - 2}px, {calculateWindEffect(1.8, 170) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
  
  <!-- Upper fruits -->
  <circle 
    cx="185" cy="175" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(2, 200)}px, {calculateWindEffect(1.5, 200)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="185" cy="175" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(2, 200) - 2}px, {calculateWindEffect(1.5, 200) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
  
  <circle 
    cx="115" cy="160" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(2.2, 220)}px, {calculateWindEffect(1.7, 220)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="115" cy="160" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(2.2, 220) - 2}px, {calculateWindEffect(1.7, 220) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
  
  <circle 
    cx="150" cy="140" r="6" 
    fill="url(#fruitGradient3)"
    style="
      transform: translate({calculateWindEffect(1.8, 240)}px, {calculateWindEffect(1.3, 240)}px);
      opacity: {$leafUnfurl * 0.9};
    "
  />
  
  <ellipse 
    cx="150" cy="140" rx="2" ry="1" 
    fill={fruitHighlightColor}
    opacity="0.8"
    style="
      transform: translate({calculateWindEffect(1.8, 240) - 2}px, {calculateWindEffect(1.3, 240) - 2}px);
      opacity: {$leafUnfurl * 0.7};
    "
  />
</g>
</g>
{/if}

<!-- Growth progress indicators styled as leaves -->
<g class="growth-stage-indicator" style="transform: translateY(390px); opacity: {$groundMovement};">
  <path 
    d="M115 0 C113 -3, 117 -6, 120 -3 C123 0, 122 3, 118 3 C114 3, 113 0, 115 0 Z" 
    fill={growthStage === 0 ? leafLightColor : "#D1D5DB"}
    stroke={growthStage === 0 ? leafDarkColor : "#9CA3AF"}
    stroke-width="0.5"
  />
  
  <path 
    d="M135 0 C133 -3, 137 -6, 140 -3 C143 0, 142 3, 138 3 C134 3, 133 0, 135 0 Z" 
    fill={growthStage === 1 ? leafLightColor : "#D1D5DB"}
    stroke={growthStage === 1 ? leafDarkColor : "#9CA3AF"}
    stroke-width="0.5"
  />
  
  <path 
    d="M155 0 C153 -3, 157 -6, 160 -3 C163 0, 162 3, 158 3 C154 3, 153 0, 155 0 Z" 
    fill={growthStage === 2 ? leafLightColor : "#D1D5DB"}
    stroke={growthStage === 2 ? leafDarkColor : "#9CA3AF"}
    stroke-width="0.5"
  />
  
  <path 
    d="M175 0 C173 -3, 177 -6, 180 -3 C183 0, 182 3, 178 3 C174 3, 173 0, 175 0 Z" 
    fill={growthStage === 3 ? leafLightColor : "#D1D5DB"}
    stroke={growthStage === 3 ? leafDarkColor : "#9CA3AF"}
    stroke-width="0.5"
  />
</g>
</svg>
</div>

<style>
.plant-container {
  width: 300px;
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  user-select: none;
  transition: transform 0.3s ease;
  position: relative;
}

.plant-container:hover {
  transform: scale(1.02);
}

.plant-container:active {
  transform: scale(0.98);
}

.plant-container::after {
  content: '';
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  width: 70%;
  height: 10px;
  background: rgba(0, 0, 0, 0.15);
  border-radius: 50%;
  filter: blur(5px);
  opacity: 0.5;
  transition: all 0.3s ease;
}

.plant-container:hover::after {
  width: 75%;
  opacity: 0.6;
}
</style>