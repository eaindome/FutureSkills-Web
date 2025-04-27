<script lang="ts">
  export let size: 'sm' | 'md' | 'lg' = "md";
  export let variant: 'light' | 'dark' = "dark";
  
  const sizes: { [key in 'sm' | 'md' | 'lg']: string } = {
    sm: "h-8 w-8",
    md: "h-12 w-12",
    lg: "h-16 w-16"
  };
  
  const textSizes: { [key in 'sm' | 'md' | 'lg']: string } = {
    sm: "text-lg",
    md: "text-2xl",
    lg: "text-3xl"
  };
  
  const sizeClass = sizes[size] || sizes.md;
  const textSizeClass = textSizes[size] || textSizes.md;
</script>

<div class="flex items-center">
  <div class={`${sizeClass} rounded-full flex items-center justify-center mr-2 shadow-md 
    hover:shadow-lg transition-all duration-300 hover:scale-105 
    bg-gradient-to-br from-green-600 to-teal-500`}>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
      class="w-2/3 h-2/3 text-white">
      <path d="M11.584 2.376a.75.75 0 01.832 0l9 6a.75.75 0 11-.832 1.248L12 3.901 3.416 9.624a.75.75 0 01-.832-1.248l9-6z" />
      <path fill-rule="evenodd" d="M20.25 10.332v9.918H21a.75.75 0 010 1.5H3a.75.75 0 010-1.5h.75v-9.918a.75.75 0 01.634-.74A49.109 49.109 0 0112 9c2.59 0 5.134.202 7.616.592a.75.75 0 01.634.74z" clip-rule="evenodd" />
    </svg>
  </div>
  <div>
    <span class={`${textSizeClass} font-bold bg-gradient-to-r from-green-700 to-teal-600 bg-clip-text text-transparent`}>
      FutureSkills
    </span>
    <span class={`${textSizeClass} font-medium ${variant === 'light' ? 'text-white/90' : 'text-gray-700'}`}>
      Coach
    </span>
  </div>
</div>