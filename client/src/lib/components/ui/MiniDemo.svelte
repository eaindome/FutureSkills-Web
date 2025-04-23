<script lang="ts">
	import { fade, fly, slide } from 'svelte/transition';
	import { onMount } from 'svelte';

	// Mock demo steps
	let currentStep = 0;
	let isVisible = false;

	const steps = [
		{
			title: 'Career Risk Analyzer',
			description: "Assess your job's automation risk and identify vulnerable areas",
			preview: {
				jobTitle: 'Retail Cashier',
				riskScore: 78,
				analysis:
					'High automation risk due to self-checkout and cashierless technology adoption across the retail sector.'
			}
		},
		{
			title: 'Green Job Pathfinder',
			description: 'Discover sustainable careers aligned with your existing skills',
			preview: {
				recommendedJobs: [
					'Solar Installation Technician (+15% growth by 2030)',
					'Green Retail Manager (+8% growth by 2030)',
					'Sustainable Supply Chain Specialist (+12% growth by 2030)'
				]
			}
		},
		{
			title: 'Reskilling & Side Hustle',
			description: 'Find training opportunities and supplemental income sources',
			preview: {
				reskilling: 'Online Solar Tech Certificate (3 months, $299)',
				sideHustle: 'Eco-Friendly Product Reviewer ($150-300/month)',
				additionalOption: 'DIY Upcycled Goods Seller ($200-500/month)'
			}
		}
	];

	function nextStep() {
		if (currentStep < steps.length - 1) {
			currentStep++;
		} else {
			currentStep = 0;
		}
	}

	function prevStep() {
		if (currentStep > 0) {
			currentStep--;
		} else {
			currentStep = steps.length - 1;
		}
	}

	// Auto-advance demo (can be toggled off)
	let autoAdvance = true;
	let timer: ReturnType<typeof setInterval> | undefined = undefined;

	function startAutoAdvance() {
		if (autoAdvance) {
			timer = setInterval(() => {
				nextStep();
			}, 8000);
		}
	}

	function stopAutoAdvance() {
		clearInterval(timer);
	}

	onMount(() => {
		// Intersection observer to start animation when in view
		const observer = new IntersectionObserver(
			(entries) => {
				if (entries[0].isIntersecting) {
					isVisible = true;
					startAutoAdvance();
				} else {
					stopAutoAdvance();
				}
			},
			{ threshold: 0.2 }
		);

		const section = document.getElementById('mini-demo');
		if (section) observer.observe(section);

		return () => {
			if (section) observer.unobserve(section);
			stopAutoAdvance();
		};
	});
</script>

<section id="mini-demo" class="relative overflow-hidden bg-gray-50 px-4 py-24 sm:px-6 lg:px-8">
	<!-- Background pattern -->
	<div class="absolute inset-0 opacity-5">
		<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
			<pattern id="demo-pattern" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
				<rect width="1" height="1" fill="#2E7D32" />
			</pattern>
			<rect width="100%" height="100%" fill="url(#demo-pattern)" />
		</svg>
	</div>

	<div class="relative mx-auto max-w-7xl">
		{#if isVisible}
			<div class="mb-16 text-center" in:fly={{ y: 30, duration: 600 }}>
				<h2 class="mb-4 text-4xl font-bold text-gray-800">See It In Action</h2>
				<div class="mx-auto mb-6 h-1 w-24 bg-green-600"></div>
				<p class="mx-auto max-w-2xl text-lg text-gray-600">
					Experience how our platform analyzes your career and offers sustainable alternatives
					tailored to your skills
				</p>
			</div>

			<div
				class="mx-auto max-w-4xl transform overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-xl transition-all duration-500"
				in:fly={{ y: 50, duration: 800, delay: 200 }}
			>
				<!-- Demo header -->
				<div class="bg-gradient-to-r from-green-600 to-teal-600 p-4 text-white">
					<div class="flex items-center">
						<div class="flex space-x-2">
							<div class="h-3 w-3 rounded-full bg-red-500"></div>
							<div class="h-3 w-3 rounded-full bg-amber-500"></div>
							<div class="h-3 w-3 rounded-full bg-green-300"></div>
						</div>
						<div class="mx-auto font-medium">FutureSkills Coach Demo</div>
						<div class="flex items-center text-xs">
							<label class="inline-flex cursor-pointer items-center">
								<input
									type="checkbox"
									bind:checked={autoAdvance}
									class="peer sr-only"
									on:change={autoAdvance ? startAutoAdvance : stopAutoAdvance}
								/>
								<div
									class="peer relative h-5 w-9 rounded-full bg-white/30 peer-checked:bg-white/60 after:absolute after:top-[2px] after:left-[2px] after:h-4 after:w-4 after:rounded-full after:bg-white after:transition-all after:content-[''] peer-checked:after:translate-x-full"
								></div>
								<span class="ml-2">Auto</span>
							</label>
						</div>
					</div>
				</div>

				<!-- Demo content -->
				<div class="flex flex-col p-6 md:p-8">
					<div class="mb-6 flex items-center justify-between">
						<h3 class="text-xl font-bold text-gray-800 md:text-2xl">{steps[currentStep].title}</h3>
						<div class="text-sm text-gray-500">Step {currentStep + 1} of {steps.length}</div>
					</div>

					<p class="mb-6 text-gray-600">{steps[currentStep].description}</p>

					<!-- Dynamic preview content based on current step -->
					<div
						class="flex-grow overflow-auto rounded-xl border border-gray-200 bg-gray-50 p-6 shadow-inner"
					>
						{#key currentStep}
							<div in:fade={{ duration: 300 }}>
								{#if currentStep === 0}
									<div class="mb-4">
										<span class="font-medium text-gray-600">Job Title:</span>
										<span class="ml-2 font-semibold text-gray-800">{steps[0].preview.jobTitle}</span
										>
									</div>
									<div class="mb-6">
										<span class="font-medium text-gray-600">Automation Risk:</span>
										<div class="relative mt-2 pt-1">
											<div class="mb-2 flex items-center justify-between">
												<div>
													<span
														class="inline-block rounded-full bg-red-600 px-3 py-1 text-sm font-bold text-white uppercase shadow"
													>
														{steps[0].preview.riskScore}% HIGH RISK
													</span>
												</div>
											</div>
											<div class="flex h-3 overflow-hidden rounded-full bg-gray-200 text-xs">
												<div
													style="width:{steps[0].preview.riskScore}%"
													class="flex animate-pulse flex-col justify-center bg-gradient-to-r from-red-500 to-red-700 text-center whitespace-nowrap text-white shadow-none"
													in:slide={{ duration: 1000, axis: 'x' }}
												></div>
											</div>
										</div>
									</div>
									<div
										class="rounded-lg border border-gray-200 bg-white p-4 text-gray-700 shadow-sm"
									>
										<span class="font-medium text-gray-600">Analysis:</span>
										<p class="mt-2">{steps[0].preview.analysis}</p>
										<div class="mt-4 flex items-center text-xs text-amber-600">
											<svg
												xmlns="http://www.w3.org/2000/svg"
												class="mr-1 h-4 w-4"
												fill="none"
												viewBox="0 0 24 24"
												stroke="currentColor"
											>
												<path
													stroke-linecap="round"
													stroke-linejoin="round"
													stroke-width="2"
													d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
												/>
											</svg>
											<span
												>Most retail cashier positions expected to decrease by 25% in the next
												decade</span
											>
										</div>
									</div>
								{:else if currentStep === 1}
									<div class="mb-4">
										<span class="font-medium text-gray-600">Recommended Green Jobs:</span>
										<ul class="mt-3 space-y-3">
											{#each steps[1].preview.recommendedJobs ?? [] as job, i}
												<li
													class="flex items-start rounded-lg border border-gray-200 bg-white p-3 shadow-sm"
													in:fly={{ y: 10, duration: 300, delay: i * 150 }}
												>
													<div
														class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-green-100"
													>
														<svg
															xmlns="http://www.w3.org/2000/svg"
															class="h-6 w-6 text-green-600"
															viewBox="0 0 20 20"
															fill="currentColor"
														>
															<path
																fill-rule="evenodd"
																d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
																clip-rule="evenodd"
															/>
														</svg>
													</div>
													<span class="text-gray-800">{job}</span>
												</li>
											{/each}
										</ul>
									</div>
									<div class="mt-4 rounded-lg border border-gray-200 bg-white p-4 shadow-sm">
										<span class="font-medium text-gray-600">Skills Match:</span>
										<div class="relative mt-2 pt-1">
											<div class="mb-2 flex items-center justify-between">
												<div>
													<span
														class="inline-block rounded-full bg-green-600 px-3 py-1 text-sm font-bold text-white uppercase"
													>
														85% STRONG MATCH
													</span>
												</div>
											</div>
											<div class="flex h-3 overflow-hidden rounded-full bg-gray-200 text-xs">
												<div
													style="width:85%"
													class="flex flex-col justify-center bg-gradient-to-r from-green-500 to-green-700 text-center whitespace-nowrap text-white shadow-none"
													in:slide={{ duration: 1000, axis: 'x' }}
												></div>
											</div>
										</div>
										<p class="mt-3 text-sm text-gray-600">
											Your customer service and organizational skills transfer well to these green
											roles
										</p>
									</div>
								{:else}
									<div class="grid grid-cols-1 gap-4 md:grid-cols-2">
										<div
											class="rounded-lg border border-gray-200 bg-white p-4 shadow-sm"
											in:fly={{ x: -20, duration: 400 }}
										>
											<div class="mb-3 flex items-start">
												<div
													class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-blue-100"
												>
													<svg
														xmlns="http://www.w3.org/2000/svg"
														class="h-6 w-6 text-blue-600"
														fill="none"
														viewBox="0 0 24 24"
														stroke="currentColor"
													>
														<path d="M12 14l9-5-9-5-9 5 9 5z" />
														<path
															d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"
														/>
														<path
															stroke-linecap="round"
															stroke-linejoin="round"
															stroke-width="2"
															d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"
														/>
													</svg>
												</div>
												<span class="font-medium text-gray-800">Recommended Training</span>
											</div>
											<div class="ml-3 border-l-4 border-blue-200 pl-2">
												<div class="font-medium text-gray-800">{steps[2].preview.reskilling}</div>
												<div class="mt-1 text-sm text-gray-600">
													Earn a certification that qualifies you for entry-level solar installation
													positions
												</div>
												<!-- svelte-ignore a11y_invalid_attribute -->
												<a
													href="#"
													class="mt-3 inline-flex items-center text-sm text-blue-600 hover:text-blue-800"
												>
													<span>View details</span>
													<svg
														xmlns="http://www.w3.org/2000/svg"
														class="ml-1 h-4 w-4"
														viewBox="0 0 20 20"
														fill="currentColor"
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

										<div
											class="rounded-lg border border-gray-200 bg-white p-4 shadow-sm"
											in:fly={{ x: 20, duration: 400 }}
										>
											<div class="mb-3 flex items-start">
												<div
													class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-amber-100"
												>
													<svg
														xmlns="http://www.w3.org/2000/svg"
														class="h-6 w-6 text-amber-600"
														fill="none"
														viewBox="0 0 24 24"
														stroke="currentColor"
													>
														<path
															stroke-linecap="round"
															stroke-linejoin="round"
															stroke-width="2"
															d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
														/>
													</svg>
												</div>
												<span class="font-medium text-gray-800">Income While Training</span>
											</div>
											<div class="mb-3 ml-3 border-l-4 border-amber-200 pl-2">
												<div class="font-medium text-gray-800">{steps[2].preview.sideHustle}</div>
												<div class="mt-1 text-sm text-gray-600">
													Leverage your retail experience to review eco-friendly products online
												</div>
											</div>
											<div class="ml-3 border-l-4 border-amber-200 pl-2">
												<div class="font-medium text-gray-800">
													{steps[2].preview.additionalOption}
												</div>
												<div class="mt-1 text-sm text-gray-600">
													Create and sell upcycled products through online marketplaces
												</div>
												<!-- svelte-ignore a11y_invalid_attribute -->
												<a
													href="#"
													class="mt-3 inline-flex items-center text-sm text-amber-600 hover:text-amber-800"
												>
													<span>Explore more options</span>
													<svg
														xmlns="http://www.w3.org/2000/svg"
														class="ml-1 h-4 w-4"
														viewBox="0 0 20 20"
														fill="currentColor"
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
							</div>
						{/key}
					</div>

					<!-- Demo navigation -->
					<div class="mt-6 flex justify-between">
						<button
							on:click={prevStep}
							class="flex items-center rounded-lg border border-gray-300 px-4 py-2 text-gray-700 shadow-sm transition-colors hover:bg-gray-100"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="mr-1 h-4 w-4"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 19l-7-7 7-7"
								/>
							</svg>
							Previous
						</button>
						<div class="flex items-center space-x-3">
							{#each steps as _, i}
								<button
									class="h-3 w-3 rounded-full transition-all {i === currentStep
										? 'scale-125 bg-green-600'
										: 'bg-gray-300 hover:bg-gray-400'}"
									on:click={() => (currentStep = i)}
									aria-label="Go to step {i + 1}"
								></button>
							{/each}
						</div>
						<button
							on:click={nextStep}
							class="flex items-center rounded-lg border border-green-600 bg-green-600 px-4 py-2 text-white shadow-sm transition-colors hover:bg-green-700"
						>
							Next
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="ml-1 h-4 w-4"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9 5l7 7-7 7"
								/>
							</svg>
						</button>
					</div>
				</div>
			</div>

			<div class="mt-12 text-center" in:fade={{ duration: 600, delay: 1000 }}>
				<a
					href="/input"
					class="inline-flex transform items-center rounded-lg border border-transparent bg-gradient-to-r from-green-600 to-teal-600 px-6 py-3 text-lg font-medium text-white shadow-md transition-all hover:scale-105 hover:from-green-700 hover:to-teal-700 focus:ring-2 focus:ring-green-500 focus:ring-offset-2 focus:outline-none"
				>
					Get Started
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="ml-2 h-5 w-5"
						viewBox="0 0 20 20"
						fill="currentColor"
					>
						<path
							fill-rule="evenodd"
							d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z"
							clip-rule="evenodd"
						/>
					</svg>
				</a>

				<p class="mx-auto mt-4 max-w-lg text-sm text-gray-500">
					Our full demo includes personalized recommendations, detailed analysis, and interactive
					tools to guide your career transition
				</p>
			</div>
		{/if}
	</div>
</section>
