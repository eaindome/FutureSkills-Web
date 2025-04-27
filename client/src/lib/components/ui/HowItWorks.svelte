<script lang="ts">
	import { fly, fade, scale } from 'svelte/transition';
	import { onMount } from 'svelte';

	let visible = false;
	let activeFeature = 0;

	onMount(() => {
		visible = true;

		// Auto-rotate features every 4 seconds
		// const in 
	});

	const features: Array<{
		title: string;
		description: string;
		icon: string;
		color: keyof typeof colorClasses;
		stats: Array<{ label: string; value: string }>;
	}> = [
		{
			title: 'Analyze',
			description:
				"Assess your job's automation risk with our AI engine that evaluates your current role against future trends and technological advancements.",
			icon: 'analyze',
			color: 'blue',
			stats: [
				{ label: 'Jobs analyzed', value: '10M+' },
				{ label: 'Accuracy rate', value: '94%' }
			]
		},
		{
			title: 'Discover',
			description:
				'Find sustainable jobs that match your skills and interests with personalized green career recommendations based on your unique profile.',
			icon: 'discover',
			color: 'green',
			stats: [
				{ label: 'Green jobs database', value: '50K+' },
				{ label: 'Matching precision', value: '87%' }
			]
		},
		{
			title: 'Transition',
			description:
				'Get personalized reskilling paths and side hustle opportunities to ensure financial stability during your career evolution.',
			icon: 'transition',
			color: 'amber',
			stats: [
				{ label: 'Skill paths', value: '2,500+' },
				{ label: 'Side hustle options', value: '1,200+' }
			]
		}
	];

	const setActive = (index: number) => {
		activeFeature = index;
	};

	// Pre-define static class mappings for colors to avoid dynamic class generation issues
	const colorClasses = {
		blue: {
			bgColor: '#3b82f6', 
			tab: 'bg-blue-500 text-white shadow-md',
			iconBg: 'bg-blue-50',
			iconGradient: 'bg-gradient-to-br from-blue-500 to-blue-600',
			title: 'text-blue-700',
			stat: 'text-blue-600',
			bulletBg: 'bg-blue-100',
			bulletDot: 'bg-blue-500',
			button: 'bg-blue-500 hover:bg-blue-600'
		},
		green: {
			bgColor: '#22c55e',
			tab: 'bg-green-500 text-white shadow-md',
			iconBg: 'bg-green-50',
			iconGradient: 'bg-gradient-to-br from-green-500 to-green-600',
			title: 'text-green-700',
			stat: 'text-green-600',
			bulletBg: 'bg-green-100',
			bulletDot: 'bg-green-500',
			button: 'bg-green-500 hover:bg-green-600'
		},
		amber: {
			bgColor: '#f59e0b',
			tab: 'bg-amber-500 text-white shadow-md',
			iconBg: 'bg-amber-50',
			iconGradient: 'bg-gradient-to-br from-amber-500 to-amber-600',
			title: 'text-amber-700',
			stat: 'text-amber-600',
			bulletBg: 'bg-amber-100',
			bulletDot: 'bg-amber-500',
			button: 'bg-amber-500 hover:bg-amber-600'
		}
	};
</script>

<section id="how-it-works" class="relative overflow-hidden bg-white px-4 py-20 sm:px-6 lg:px-8">
	<!-- Background decoration -->
	<div class="absolute inset-0 overflow-hidden">
		<div
			class="absolute top-1/4 right-0 h-96 w-96 rounded-full bg-green-50 opacity-30 mix-blend-multiply blur-3xl filter"
		></div>
		<div
			class="absolute bottom-0 left-1/4 h-96 w-96 rounded-full bg-blue-50 opacity-30 mix-blend-multiply blur-3xl filter"
		></div>
	</div>

	<div class="relative mx-auto max-w-7xl">
		<div class="mb-16 text-center">
			{#if visible}
				<div in:fly={{ y: 20, duration: 600 }}>
					<p class="mb-2 font-medium text-green-600">3-Step Process</p>
					<h2 class="mb-4 text-3xl font-bold text-gray-800 md:text-4xl lg:text-5xl">
						How It Works
					</h2>
					<div class="mx-auto mb-6 h-1 w-24 bg-gradient-to-r from-green-500 to-teal-500"></div>
					<p class="mx-auto max-w-2xl text-lg text-gray-600">
						Our AI-powered platform guides you through three simple steps to secure your future in
						green industries
					</p>
				</div>
			{/if}
		</div>

		<!-- Features with animated tabs -->
		<div class="mb-16">
			{#if visible}
				<div class="mb-8 flex justify-center" in:fly={{ y: 20, duration: 600, delay: 200 }} out:fly={{ y: -20, duration: 300 }}>
					<div class="relative inline-flex rounded-xl bg-gray-100 p-1.5 shadow-inner overflow-hidden">
					<!-- Animated background indicator -->
					<div
						class="absolute top-1.5 bottom-1.5 transition-all duration-400 ease-in-out rounded-lg shadow-md"
						style={`
						width: ${100 / features.length - 2}%;
						left: calc(${activeFeature * (100 / features.length)}% + 0.375rem);
						background: ${colorClasses[features[activeFeature].color].bgColor};
						transform: translateX(0);
						`}
					></div>
					
					{#each features as feature, i}
						<button
						on:click={() => setActive(i)}
						class={`relative rounded-lg px-6 py-3 font-medium z-10 transition-all duration-300 flex items-center justify-center ${
							activeFeature === i
							? 'text-white'
							: 'text-gray-600 hover:text-gray-800'
						}`}
						style={`width: ${100 / features.length}%;`}
						>
						
						<!-- Text with subtle transition -->
						<span class="transition-all duration-300 transform ${
							activeFeature === i ? 'scale-105' : 'scale-100'
						}">{feature.title}</span>
						
						<!-- Optional: Add subtle indicator dot for active state -->
						{#if activeFeature === i}
							<span class="absolute -bottom-0.5 left-1/2 transform -translate-x-1/2 w-1 h-1 bg-white rounded-full"></span>
						{/if}
						</button>
					{/each}
					</div>
			  </div>

				<!-- Feature showcase -->
				<div class="mx-auto max-w-4xl overflow-hidden rounded-2xl bg-white shadow-xl">
					{#each features as feature, i}
						{#if activeFeature === i}
							<div class="grid gap-6 md:grid-cols-5" in:fade={{ duration: 400 }}>
								<!-- Icon column -->
								<div
									class={`md:col-span-2 ${colorClasses[feature.color].iconBg} flex flex-col items-center justify-center p-8`}
								>
									<div
										class={`h-24 w-24 rounded-2xl ${colorClasses[feature.color].iconGradient} mb-6 flex transform items-center justify-center shadow-lg transition-transform duration-500 hover:scale-110 hover:rotate-3`}
									>
										{#if feature.icon === 'analyze'}
											<svg
												xmlns="http://www.w3.org/2000/svg"
												class="h-12 w-12 text-white"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													stroke-width="2"
													d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
												/>
											</svg>
										{:else if feature.icon === 'discover'}
											<svg
												xmlns="http://www.w3.org/2000/svg"
												class="h-12 w-12 text-white"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													stroke-width="2"
													d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
												/>
											</svg>
										{:else}
											<svg
												xmlns="http://www.w3.org/2000/svg"
												class="h-12 w-12 text-white"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													stroke-width="2"
													d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
												/>
											</svg>
										{/if}
									</div>

									<h3
										class={`text-2xl font-bold ${colorClasses[feature.color].title} mb-2 text-center`}
									>
										{feature.title}
									</h3>

									<!-- Stats -->
									<div class="mt-4 grid w-full grid-cols-2 gap-4">
										{#each feature.stats as stat}
											<div class="text-center">
												<p class={`${colorClasses[feature.color].stat} text-xl font-bold`}>
													{stat.value}
												</p>
												<p class="text-sm text-gray-500">{stat.label}</p>
											</div>
										{/each}
									</div>
								</div>

								<!-- Content column -->
								<div class="p-8 md:col-span-3">
									<h4 class="mb-4 text-xl font-bold text-gray-800">
										Step {i + 1}: {feature.title}
									</h4>
									<p class="mb-6 text-gray-600">{feature.description}</p>

									<!-- Feature bullets -->
									<ul class="space-y-3">
										{#if feature.icon === 'analyze'}
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>AI-powered risk assessment customized to your job</p>
											</li>
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Visualized risk scores with detailed insights</p>
											</li>
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Industry trend analysis to understand future impact</p>
											</li>
										{:else if feature.icon === 'discover'}
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Personalized green job recommendations</p>
											</li>
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Growth forecasts for sustainable industries</p>
											</li>
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Skills transferability mapping to green sectors</p>
											</li>
										{:else}
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Tailored reskilling pathways and course recommendations</p>
											</li>
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Side hustle suggestions matched to your skills</p>
											</li>
											<li class="flex items-start">
												<div
													class={`mt-1 mr-3 h-5 w-5 flex-shrink-0 rounded-full ${colorClasses[feature.color].bulletBg} flex items-center justify-center`}
												>
													<div
														class={`h-2 w-2 rounded-full ${colorClasses[feature.color].bulletDot}`}
													></div>
												</div>
												<p>Guided transition planning with financial stability focus</p>
											</li>
										{/if}
									</ul>

									<div class="mt-6">
										<a 
										  href="/about"
										  class={`
											group inline-flex items-center gap-2 rounded-lg px-5 py-2.5
											${colorClasses[feature.color].button} text-white
											shadow-md hover:shadow-lg
											transform transition-all duration-300 hover:-translate-y-1
											focus:outline-none focus:ring-2 focus:ring-offset-2 ${colorClasses[feature.color].bgColor || 'focus:ring-opacity-50'}
										  `}
										>
										  <span class="font-medium">Learn more</span>
										  <svg
											xmlns="http://www.w3.org/2000/svg"
											class="h-4 w-4 transform transition-transform duration-300 group-hover:translate-x-1"
											viewBox="0 0 20 20"
											fill="currentColor"
											aria-hidden="true"
										  >
											<path
											  fill-rule="evenodd"
											  d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
											  clip-rule="evenodd"
											/>
										  </svg>
										</a>
									  </div>
								</div>
							</div>
						{/if}
					{/each}
				</div>
			{/if}
		</div>

		<!-- Progress steps visualization -->
		<div class="mt-12 flex justify-center">
			{#if visible}
				<div class="relative" in:fly={{ y: 20, duration: 600, delay: 800 }}>
					<div class="flex items-center">
						<!-- Step 1 -->
						<div class="relative flex flex-col items-center">
							<div
								class={`h-12 w-12 rounded-full border-4 ${activeFeature === 0 ? 'border-blue-500 bg-blue-100' : 'border-gray-200 bg-white'} mb-2 flex items-center justify-center transition-all duration-300`}
							>
								<span
									class={`text-lg font-bold ${activeFeature === 0 ? 'text-blue-600' : 'text-gray-500'}`}
									>1</span
								>
							</div>
							<span
								class={`text-sm font-medium ${activeFeature === 0 ? 'text-blue-600' : 'text-gray-500'}`}
								>Analyze</span
							>
						</div>

						<!-- Connector -->
						<div
							class={`h-1 w-16 ${activeFeature >= 1 ? 'bg-green-500' : 'bg-gray-200'} transition-all duration-500`}
						></div>

						<!-- Step 2 -->
						<div class="relative flex flex-col items-center">
							<div
								class={`h-12 w-12 rounded-full border-4 ${activeFeature === 1 ? 'border-green-500 bg-green-100' : 'border-gray-200 bg-white'} mb-2 flex items-center justify-center transition-all duration-300`}
							>
								<span
									class={`text-lg font-bold ${activeFeature === 1 ? 'text-green-600' : 'text-gray-500'}`}
									>2</span
								>
							</div>
							<span
								class={`text-sm font-medium ${activeFeature === 1 ? 'text-green-600' : 'text-gray-500'}`}
								>Discover</span
							>
						</div>

						<!-- Connector -->
						<div
							class={`h-1 w-16 ${activeFeature >= 2 ? 'bg-amber-500' : 'bg-gray-200'} transition-all duration-500`}
						></div>

						<!-- Step 3 -->
						<div class="relative flex flex-col items-center">
							<div
								class={`h-12 w-12 rounded-full border-4 ${activeFeature === 2 ? 'border-amber-500 bg-amber-100' : 'border-gray-200 bg-white'} mb-2 flex items-center justify-center transition-all duration-300`}
							>
								<span
									class={`text-lg font-bold ${activeFeature === 2 ? 'text-amber-600' : 'text-gray-500'}`}
									>3</span
								>
							</div>
							<span
								class={`text-sm font-medium ${activeFeature === 2 ? 'text-amber-600' : 'text-gray-500'}`}
								>Transition</span
							>
						</div>
					</div>
				</div>
			{/if}
		</div>

		<!-- CTA -->
		<!-- {#if visible}
			<div class="mt-16 text-center" in:fly={{ y: 20, duration: 600, delay: 1000 }}>
				<a
					href="#mini-demo"
					class="group inline-flex transform items-center rounded-lg bg-gradient-to-r from-green-600 to-teal-500 px-6 py-3 font-medium text-white shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
				>
					<span>Try the Demo</span>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="ml-2 h-5 w-5 transition-transform group-hover:translate-x-1"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							fill-rule="evenodd"
							d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H3a1 1 0 110-2h9.586l-2.293-2.293a1 1 0 010-1.414z"
							clip-rule="evenodd"
						/>
					</svg>
				</a>
			</div>
		{/if} -->
	</div>
</section>

<style>
	/* Amber color classes to ensure they're included in the build */
	:global(.bg-amber-50) {
		background-color: rgba(255, 251, 235, var(--tw-bg-opacity, 1));
	}
	:global(.bg-amber-100) {
		background-color: rgba(254, 243, 199, var(--tw-bg-opacity, 1));
	}
	:global(.bg-amber-500) {
		background-color: rgba(245, 158, 11, var(--tw-bg-opacity, 1));
	}
	:global(.bg-amber-600) {
		background-color: rgba(217, 119, 6, var(--tw-bg-opacity, 1));
	}
	:global(.hover\:bg-amber-600:hover) {
		background-color: rgba(217, 119, 6, var(--tw-bg-opacity, 1));
	}
	:global(.text-amber-600) {
		color: rgba(217, 119, 6, var(--tw-text-opacity, 1));
	}
	:global(.text-amber-700) {
		color: rgba(180, 83, 9, var(--tw-text-opacity, 1));
	}
	:global(.border-amber-500) {
		border-color: rgba(245, 158, 11, var(--tw-border-opacity, 1));
	}
	:global(.from-amber-500) {
		--tw-gradient-from: rgba(245, 158, 11, var(--tw-gradient-from-opacity, 1));
	}
	:global(.to-amber-600) {
		--tw-gradient-to: rgba(217, 119, 6, var(--tw-gradient-to-opacity, 1));
	}
</style>
