<script lang="ts">
	import { fly, fade } from 'svelte/transition';
	import { onMount } from 'svelte';

    import Navbar from '$lib/components/layouts/Navbar.svelte';
	import Footer from '$lib/components/layout/Footer.svelte';

	let visible = false;
	let activeTab = 'mission';
	let activeFeature = 0;

	onMount(() => {
		visible = true;
	});

	const switchTab = (tab: string) => {
		activeTab = tab;
	};

	// Team members data
	const teamMembers = [
		{
			name: 'Alex Rivera',
			role: 'Project Lead',
			bio: 'Green tech enthusiast with 8+ years of experience in sustainable innovation and AI solutions.'
		},
		{
			name: 'Morgan Chen',
			role: 'AI Engineer',
			bio: 'Specializes in machine learning models focused on career pattern analysis and job market predictions.'
		},
		{
			name: 'Sam Johnson',
			role: 'UI/UX Designer',
			bio: 'Creates user-centered designs that make complex career data accessible and actionable.'
		}
	];

	// FAQ data
	const faqs = [
		{
			question: 'How accurate is the job risk assessment?',
			answer: 'Our AI analyzes multiple factors including industry trends, automation research, and market forecasts to provide assessments with approximately 94% alignment with expert predictions. We continuously update our models with the latest research.'
		},
		{
			question: 'What qualifies as a "green job"?',
			answer: 'We define green jobs as roles that contribute to preserving or restoring environmental quality, reducing carbon footprints, or promoting sustainability. This includes direct environmental roles (renewable energy technicians) and greened traditional jobs (sustainable supply chain managers).'
		},
		{
			question: 'How are skill paths determined?',
			answer: 'Our system maps your existing skills against those required for recommended green careers, identifying gaps and suggesting efficient learning paths based on transferable skills, time constraints, and financial considerations.'
		},
		{
			question: 'Are the side hustle suggestions realistic?',
			answer: 'Yes, all side hustle recommendations are vetted for feasibility, startup costs, and income potential. We prioritize options with low barriers to entry and those that complement your existing skills and interests.'
		},
		{
			question: 'Is my personal data secure?',
			answer: 'Absolutely. We use enterprise-grade encryption and never share your personal information with third parties. Your career data is used only to provide personalized recommendations.'
		}
	];

	// Timeline data
	const timeline = [
		{
			year: 'April 5',
			milestone: 'Project Inception',
			description: 'FutureSkills Coach was conceived in response to accelerating job displacement in traditional sectors.'
		},
		{
			year: 'April 25',
			milestone: 'Research & Development',
			description: 'Our team analyzed job market data and built initial models to predict automation risk across industries.'
		},
		{
			year: 'May 5',
			milestone: 'Call for Code Hackathon',
			description: 'Developed as a proof-of-concept submission for the UN SDG 8 (Decent Work and Economic Growth) challenge.'
		},
		{
			year: 'Future',
			milestone: 'Full Platform Launch',
			description: 'Plans to expand features, integrate with job boards, and partner with educational institutions.'
		}
	];

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

	

	// Stats data
	const impactStats = [
		{ metric: '10 Million+', label: 'Jobs analyzed for automation risk' },
		{ metric: '50,000+', label: 'Green career paths in our database' },
		{ metric: '2,500+', label: 'Skill development pathways' },
		{ metric: '1,200+', label: 'Side hustle opportunities' }
	];
</script>

<svelte:head>
  <title>About - FutureSkills Coach</title>
</svelte:head>

<Navbar isLoggedIn={false} />

<section class="relative bg-white py-20 px-4 sm:px-6 lg:px-8 ">
	<!-- Background decorations -->
	<div class="absolute inset-0 overflow-hidden">
		<div
			class="absolute top-0 left-1/4 h-96 w-96 rounded-full bg-green-50 opacity-30 mix-blend-multiply blur-3xl filter"
		></div>
		<div
			class="absolute bottom-1/3 right-1/4 h-96 w-96 rounded-full bg-blue-50 opacity-30 mix-blend-multiply blur-3xl filter"
		></div>
	</div>

	<div class="relative mx-auto max-w-7xl">
		<!-- Header -->
		{#if visible}
			<div class="mb-16 text-center" in:fly={{ y: 20, duration: 600 }}>
				<p class="mb-2 font-medium text-green-600">About Our Platform</p>
				<h1 class="mb-4 text-3xl font-bold text-gray-800 md:text-4xl lg:text-5xl">
					FutureSkills Coach
				</h1>
				<div class="mx-auto mb-6 h-1 w-24 bg-gradient-to-r from-green-500 to-teal-500"></div>
				<p class="mx-auto max-w-3xl text-lg text-gray-600">
					Empowering workers and students to thrive in the green economy through AI-driven career
					guidance, reskilling pathways, and financial stability solutions.
				</p>
			</div>
		{/if}

		<!-- Content Tabs -->
		{#if visible}
			<div class="mb-8" in:fly={{ y: 20, duration: 600, delay: 200 }} out:fly={{ y: -20, duration: 300 }}>
				<div class="relative flex flex-wrap justify-center gap-2 sm:gap-4 p-1 bg-gray-50 bg-opacity-50 rounded-xl shadow-inner mx-auto max-w-md">
				<!-- Background slider that animates between positions -->
				<div 
					class="absolute transition-all duration-300 ease-in-out rounded-lg shadow-md h-10"
					style={`
					width: calc(33.333% - 8px);
					background: ${
						activeTab === 'mission' ? '#16a34a' : 
						activeTab === 'team' ? '#f59e0b' : '#14b8a6'
					};
					left: ${activeTab === 'mission' ? '4px' : '0'};
					transform: translateX(${
						activeTab === 'mission' ? '0' : 
						activeTab === 'team' ? 'calc(100% + 8px)' : 
						'calc(200% + 16px)'
					});
					`}
				></div>
				
				<!-- Tab buttons -->
				<button
					on:click={() => switchTab('mission')}
					class="relative px-4 py-2 rounded-lg font-medium transition-all duration-300 flex-1 z-10"
					class:text-white={activeTab === 'mission'}
					class:text-gray-700={activeTab !== 'mission'}
				>
					<span class="relative z-10 transition-all duration-300">Our Mission</span>
				</button>
				
				<button
					on:click={() => switchTab('team')}
					class="relative px-4 py-2 rounded-lg font-medium transition-all duration-300 flex-1 z-10"
					class:text-white={activeTab === 'team'}
					class:text-gray-700={activeTab !== 'team'}
				>
					<span class="relative z-10 transition-all duration-300">Our Team</span>
				</button>
				
				<button
					on:click={() => switchTab('faq')}
					class="relative px-4 py-2 rounded-lg font-medium transition-all duration-300 flex-1 z-10"
					class:text-white={activeTab === 'faq'}
					class:text-gray-700={activeTab !== 'faq'}
				>
					<span class="relative z-10 transition-all duration-300">FAQ</span>
				</button>
				</div>
			</div>
		{/if}

		<!-- Tab Content -->
		<div class="overflow-hidden rounded-2xl bg-white shadow-xl">
			{#if activeTab === 'mission'}
                <div in:fade={{ duration: 300 }} class="grid md:grid-cols-2">
                    <!-- Left side - Image/Graphic -->
                    <div class="bg-gradient-to-br from-green-600 to-teal-700 p-8 overflow-hidden relative">
						<!-- Decorative background elements -->
						<div class="absolute top-0 left-0 w-full h-full overflow-hidden opacity-10">
							<div class="absolute top-0 right-0 w-64 h-64 bg-white rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
							<div class="absolute bottom-0 left-0 w-64 h-64 bg-white rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>
						</div>
					
						<div class="relative z-10 max-w-lg mx-auto">
							<!-- SDG 8 Icon - Using official SDG 8 colors (burgundy/red: #a21942) -->
							<div class="flex flex-col items-center justify-center mb-10">
								<div class="mb-4 relative">
									<div class="absolute inset-0 bg-[#a21942] rounded-full opacity-20 animate-pulse scale-110"></div>
									<div class="relative flex items-center justify-center h-28 w-28 rounded-full bg-[#a21942] shadow-lg">
										<img 
											src="/sdg8sml.png" 
											alt="SDG 8 - Decent Work and Economic Growth" 
											class="h-20 w-20 object-contain"
										/>
									</div>
								</div>
								<h3 class="text-3xl font-bold text-white mb-1">SDG 8</h3>
								<p class="text-green-50 text-lg">Decent Work and Economic Growth</p>
								<div class="mt-3 h-1 w-24 bg-white bg-opacity-30 rounded-full"></div>
							</div>
					
							<!-- Timeline with improved visual layout -->
							<div class="mb-12 relative">
								<div class="absolute left-1/2 top-2 bottom-2 w-1 -translate-x-1/2 bg-white bg-opacity-20"></div>
								
								{#each timeline as item, i}
									<div class="relative mb-10 last:mb-0">
										<!-- Year marker with improved visual -->
										<div class="absolute left-1/2 -translate-x-1/2 flex items-center justify-center">
											<div class="h-18 w-18 rounded-full border-2 border-white bg-green-700 shadow-lg flex items-center justify-center z-10 hover:scale-110 transition-transform duration-300">
												<span class="text-sm font-bold text-white">{item.year}</span>
											</div>
										</div>
										
										<!-- Content with improved card design -->
										<div class={`
											${i % 2 === 0 ? 'ml-auto pl-8 text-right' : 'mr-auto pr-8 text-left'}
											w-5/6 sm:w-5/12 pt-1
										`}>
											<div class="bg-white bg-opacity-10 backdrop-blur-sm rounded-lg p-4 shadow-lg border border-white border-opacity-20 hover:bg-opacity-20 transition-all duration-300 transform hover:-translate-y-1">
												<h4 class="text-lg font-bold text-teal-600 mb-1">{item.milestone}</h4>
												<p class="text-gray-400 font-medium">{item.description}</p>
											</div>
										</div>
									</div>
								{/each}
							</div>
							
							<!-- Stats with improved card design -->
							<!-- <h4 class="text-xl font-bold text-white mb-4 text-center">Our Impact</h4>
							<div class="grid grid-cols-2 gap-4">
								{#each impactStats.slice(0, 4) as stat}
									<div class="bg-white bg-opacity-10 backdrop-blur-sm rounded-lg p-4 shadow-lg border border-white border-opacity-20 transform transition-all duration-300 hover:-translate-y-1 hover:bg-opacity-20 text-center">
										<p class="text-2xl font-bold text-teal-600 mb-1">{stat.metric}</p>
										<p class="text-gray-500 text-opacity-90 text-sm font-semibo">{stat.label}</p>
									</div>
								{/each}
							</div> -->
						</div>
					</div>
                
                    <!-- Right side - Text content -->
                    <div class="p-8 bg-white">
                        <h2 class="mb-6 text-2xl font-bold text-gray-800 border-b border-green-200 pb-2">Our Mission & Vision</h2>
                
                        <div class="mb-6 hover:bg-green-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-green-700 flex items-center">
                                <span class="mr-2 w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                                    </svg>
                                </span>
                                The Challenge
                            </h3>
                            <p class="mb-4 text-gray-600 pl-10">
                                As automation and AI transform industries, millions of workers face job displacement while sustainable sectors struggle to fill positions due to skills mismatches. Financial barriers during career transitions further limit economic inclusion and growth.
                            </p>
                        </div>
                
                        <div class="mb-6 hover:bg-green-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-green-700 flex items-center">
								<span class="mr-2 w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                                    </svg>
                                </span>
                                Our Solution
                            </h3>
                            <p class="mb-4 text-gray-600 pl-10">
                                FutureSkills Coach bridges this gap with AI-powered tools that guide users through the complete journey from risk assessment to sustainable employment, with financial stability support along the way.
                            </p>
                        </div>
                
                        <div class="mb-6 hover:bg-green-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-green-700 flex items-center">
                                <span class="mr-2 w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                                    </svg>
                                </span>
                                Core Principles
                            </h3>
                            <ul class="space-y-3 text-gray-600 pl-10">
                                <li class="flex items-start bg-white p-2 rounded-md shadow-sm hover:shadow transition-shadow">
                                    <div class="mr-3 mt-1 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full bg-green-100">
                                        <div class="h-2 w-2 rounded-full bg-green-500"></div>
                                    </div>
                                    <p><strong class="text-green-700">Accessibility:</strong> Tools and guidance available to all, regardless of technical expertise</p>
                                </li>
                                <li class="flex items-start bg-white p-2 rounded-md shadow-sm hover:shadow transition-shadow">
                                    <div class="mr-3 mt-1 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full bg-green-100">
                                        <div class="h-2 w-2 rounded-full bg-green-500"></div>
                                    </div>
                                    <p><strong class="text-green-700">Sustainability:</strong> Focus on future-proof careers in green industries</p>
                                </li>
                                <li class="flex items-start bg-white p-2 rounded-md shadow-sm hover:shadow transition-shadow">
                                    <div class="mr-3 mt-1 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full bg-green-100">
                                        <div class="h-2 w-2 rounded-full bg-green-500"></div>
                                    </div>
                                    <p><strong class="text-green-700">Financial Stability:</strong> Income solutions during career transitions</p>
                                </li>
                                <li class="flex items-start bg-white p-2 rounded-md shadow-sm hover:shadow transition-shadow">
                                    <div class="mr-3 mt-1 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full bg-green-100">
                                        <div class="h-2 w-2 rounded-full bg-green-500"></div>
                                    </div>
                                    <p><strong class="text-green-700">Data-Driven:</strong> Recommendations based on real-world trends and forecasts</p>
                                </li>
                            </ul>
                        </div>
                
                        <div class="hover:bg-green-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-green-700 flex items-center">
                                <span class="mr-2 w-8 h-8 rounded-full bg-green-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                                    </svg>
                                </span>
                                Long-Term Vision
                            </h3>
                            <p class="text-gray-600 pl-10">
                                We aim to create a comprehensive ecosystem where workers, educators, employers, and policymakers collaborate to ensure economic inclusion in the sustainable future of work, measurably advancing UN SDG 8 targets by 2030.
                            </p>
                        </div>
                    </div>
                </div>
			{:else if activeTab === 'team'}
                <div in:fade={{ duration: 300 }} class="grid md:grid-cols-2">
                    <!-- Left side - Content -->
                    <div class="p-8 bg-white">
                        <h2 class="mb-6 text-2xl font-bold text-gray-800 border-b border-amber-200 pb-2">Our Team</h2>
                
                        <div class="mb-6 p-4 rounded-lg border-l-4 border-amber-500 bg-amber-50">
                            <p class="mb-6 text-gray-600">
                                FutureSkills Coach brings together experts in AI, career development, sustainability, and user experience design to create a platform that meaningfully addresses the future of work challenges.
                            </p>
                        </div>
                
                        <div class="mb-6 hover:bg-amber-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-amber-700 flex items-center">
                                <span class="mr-2 w-8 h-8 rounded-full bg-amber-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                                    </svg>
                                </span>
                                Our Commitment
                            </h3>
                            <p class="text-gray-600 pl-10">
                                We're dedicated to democratizing access to career transition tools and ensuring no worker is left behind in the shift to a sustainable economy. Our diverse team brings perspectives from workforce development, technology, and environmental sectors.
                            </p>
                        </div>
                
                        <div class="mb-6 hover:bg-amber-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-amber-700 flex items-center">
                                <span class="mr-2 w-8 h-8 rounded-full bg-amber-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                                    </svg>
                                </span>
                                Developed For Call for Code
                            </h3>
                            <p class="text-gray-600 pl-10">
                                This project was created as part of the 2025 Call for Code Hackathon, addressing the UN Sustainable Development Goal 8: Decent Work and Economic Growth. We leveraged IBM Granite models to create an AI-driven solution that can make a real difference in people's lives and livelihoods.
                            </p>
                        </div>
                
                        <div class="hover:bg-amber-50 p-4 rounded-lg transition-colors">
                            <h3 class="mb-2 text-xl font-semibold text-amber-700 flex items-center">
                                <span class="mr-2 w-8 h-8 rounded-full bg-amber-100 flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                                    </svg>
                                </span>
                                Looking Forward
                            </h3>
                            <p class="text-gray-600 pl-10">
                                Beyond the hackathon, we envision growing this platform into a comprehensive ecosystem connecting workers, educators, and employers to create sustainable career pathways at scale.
                            </p>
                        </div>
                    </div>
                
                    <!-- Right side - Team members -->
                    <div class="bg-gradient-to-br from-amber-500 to-amber-600 p-8">
                        <h2 class="mb-8 text-2xl font-bold text-white flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                            </svg>
                            Meet The Team
                        </h2>
                    
                        <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                            {#each teamMembers as member}
                            <div class="overflow-hidden rounded-xl bg-white shadow-lg transition-all duration-300 transform hover:-translate-y-1 hover:shadow-xl">
                                <!-- Top visual element - decorative wave or pattern -->
                                <div class="relative h-16 bg-gradient-to-r from-amber-400 to-amber-500">
                                    <div class="absolute bottom-0 left-0 right-0">
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" class="w-full h-8">
                                            <path fill="#ffffff" fill-opacity="1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,138.7C960,139,1056,117,1152,117.3C1248,117,1344,139,1392,149.3L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
                                        </svg>
                                    </div>
                                </div>
                                
                                <!-- Content section with avatar -->
                                <div class="px-6 pb-6 text-center">
                                    <!-- Avatar circle that overlaps the wave -->
                                    <div class="relative -mt-10 mb-4">
                                        <div class="inline-flex h-20 w-20 items-center justify-center rounded-full border-4 border-white bg-amber-100 shadow">
                                            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                            </svg>
                                        </div>
                                    </div>
                                    
                                    <!-- Text content -->
                                    <h3 class="mb-1 text-xl font-bold text-gray-800">{member.name}</h3>
                                    <p class="mb-3 text-sm font-medium text-amber-600">{member.role}</p>
                                    
                                    <!-- Subtle divider -->
                                    <div class="h-0.5 w-12 mx-auto mb-4 bg-gradient-to-r from-amber-300 to-amber-500 rounded-full"></div>
                                    
                                    <!-- Bio with left-aligned text in a container -->
                                    <div class="bg-amber-50 rounded-lg p-4 text-left">
                                        <p class="text-gray-700">{member.bio}</p>
                                    </div>
                                </div>
                            </div>
                            {/each}
                        </div>
                    
                        <div class="mt-12">
                            <h3 class="mb-6 text-xl font-semibold text-white flex items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 20V10M12 20V4M6 20v-6" />
                                </svg>
                                Partners & Supporters
                            </h3>
                            
                            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                                <!-- IBM -->
                                <div class="bg-white rounded-lg p-4 shadow-md hover:shadow-lg transition-all flex items-center justify-center">
                                    <div class="h-16 flex items-center justify-center">
                                        <div class="text-center">
                                            <div class="h-12 w-16 mx-auto mb-2 bg-[#0043CE] rounded-md flex items-center justify-center shadow-sm" style="background-color: #0043CE;">
                                                <span class="text-lg font-bold text-white">IBM</span>
                                            </div>
                                            <p class="text-sm font-medium text-gray-700">Technology</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- UN -->
                                <div class="bg-white rounded-lg p-4 shadow-md hover:shadow-lg transition-all flex items-center justify-center">
                                    <div class="h-16 flex items-center justify-center">
                                        <div class="text-center">
                                            <div class="h-12 w-16 mx-auto mb-2 bg-[#4B92DB] !important rounded-md flex items-center justify-center shadow-sm" style="background-color: #4B92DB;">
                                                <span class="text-lg font-bold text-white">UN</span>
                                            </div>
                                            <p class="text-sm font-medium text-gray-700">Framework</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Call for Code -->
                                <div class="bg-white rounded-lg p-4 shadow-md hover:shadow-lg transition-all flex items-center justify-center" >
                                    <div class="h-16 flex items-center justify-center">
                                        <div class="text-center">
                                            <div class="h-12 w-16 mx-auto mb-2 bg-[#FF7A59] rounded-md flex items-center justify-center shadow-sm" style="background-color: #FF7A59;">
                                                <span class="text-xs font-bold text-white">CfC</span>
                                            </div>
                                            <p class="text-sm font-medium text-gray-700">Initiative</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- SDG 8 -->
                                <div class="bg-white rounded-lg p-4 shadow-md hover:shadow-lg transition-all flex items-center justify-center">
                                    <div class="h-16 flex items-center justify-center">
                                        <div class="text-center">
                                            <div class="h-12 w-16 mx-auto mb-2 bg-[#8F1838] rounded-md flex items-center justify-center shadow-sm" style="background-color: #8F1838;">
                                                <span class="text-xs font-bold text-white">SDG 8</span>
                                            </div>
                                            <p class="text-sm font-medium text-gray-700">UN Goal</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
			{:else if activeTab === 'faq'}
				<div in:fade={{ duration: 300 }} class="grid md:grid-cols-2">
					<!-- FAQ side -->
					<div class="p-8">
						<h2 class="mb-6 text-2xl font-bold text-gray-800">Frequently Asked Questions</h2>

						<div class="space-y-6">
							{#each faqs as faq, i}
								<div>
									<h3 class="mb-2 text-lg font-semibold text-teal-700">{faq.question}</h3>
									<p class="text-gray-600">{faq.answer}</p>
								</div>

								{#if i < faqs.length - 1}
									<div class="border-b border-gray-200"></div>
								{/if}
							{/each}
						</div>
				</div>

					<!-- Contact & Support side -->
					<div class="bg-gradient-to-br from-teal-500 to-teal-700 p-8 rounded-lg shadow-lg">
						<h2 class="mb-6 text-2xl font-bold text-white flex items-center">
						<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
						</svg>
						Get in Touch
						</h2>
					
						<!-- Contact Cards -->
						<div class="mb-8 rounded-lg bg-white bg-opacity-10 p-6 backdrop-blur-sm hover:bg-opacity-15 transition-all duration-300">
						<h3 class="mb-4 text-xl font-semibold text-teal-600 border-b border-teal-400 pb-2 inline-block">Contact Us</h3>
						
						<div class="grid md:grid-cols-2 gap-4">
							<!-- Email Contact -->
							<div class="flex items-start bg-white bg-opacity-5 p-4 rounded-lg hover:bg-opacity-10 transition-all">
								<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-teal-500 bg-opacity-20">
									<svg
									xmlns="http://www.w3.org/2000/svg"
									class="h-5 w-5 text-white"
									fill="none"
									viewBox="0 0 24 24"
									stroke="currentColor"
									>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
									/>
									</svg>
								</div>
							<div>
								<p class="font-medium text-teal-700">Email Us</p>
								<a href="mailto:contact@futureskillscoach.org" class="text-teal-600 hover:text-white transition-colors">contact@futureskillscoach.org</a>
							</div>
							</div>
							
							<!-- Support Contact -->
							<div class="flex items-start bg-white bg-opacity-5 p-4 rounded-lg hover:bg-opacity-10 transition-all">
							<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-teal-500 bg-opacity-20">
								<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-5 w-5 text-white"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"
								/>
								</svg>
							</div>
							<div>
								<p class="font-medium text-teal-700">Support Hours</p>
								<p class="text-teal-600">Monday-Friday, 9am-5pm ET</p>
							</div>
							</div>
							
							<!-- Help Center -->
							<div class="flex items-start bg-white bg-opacity-5 p-4 rounded-lg hover:bg-opacity-10 transition-all">
							<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-teal-500 bg-opacity-20">
								<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-5 w-5 text-white"
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
							</div>
							<div>
								<p class="font-medium text-teal-700">Help Center</p>
								<a href="#BrowseResources" class="text-teal-600 hover:text-white transition-colors">Browse resources</a>
							</div>
							</div>
							
							<!-- Social Media -->
							<div class="flex items-start bg-white bg-opacity-5 p-4 rounded-lg hover:bg-opacity-10 transition-all">
							<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-teal-500 bg-opacity-20">
								<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-5 w-5 text-white"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
								>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14"
								/>
								</svg>
							</div>
							<div>
								<p class="font-medium text-teal-700">Connect With Us</p>
								<div class="flex space-x-2 mt-1">
								<a href="/valid-url" class="text-teal-500 hover:text-white transition-colors" aria-label="Visit our social media page">
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
									<path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
									</svg>
								</a>
								<a href="/valid-url" class="text-teal-500 hover:text-white transition-colors" aria-label="Visit our social media page">
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
									<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
									</svg>
								</a>
								<a href="/valid-url" class="text-teal-500 hover:text-white transition-colors" aria-label="Visit our social media page">
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
									<path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
									</svg>
								</a>
								</div>
							</div>
							</div>
						</div>
						</div>
					
						<!-- Newsletter Signup -->
						<div class="rounded-lg bg-white bg-opacity-10 p-6 backdrop-blur-sm hover:bg-opacity-15 transition-all duration-300">
						<h3 class="mb-4 text-xl font-semibold text-teal-600 border-b border-teal-400 pb-2 inline-block">Join Our Mission</h3>
						
						<p class="mb-4 text-teal-600">
							Sign up for updates about platform improvements, new features, and opportunities to contribute to our work.
						</p>
						
						<form class="space-y-4">
							<div class="flex flex-col sm:flex-row gap-3">
								<input
									type="email"
									placeholder="Your email address"
									class="flex-1 rounded-lg border-1 border-teal-500 bg-white bg-opacity-20 p-3 text-gray-500 placeholder-teal-800 focus:outline-none focus:ring-2 focus:ring-teal-500"
									required
								/>
								
								<button
									type="submit"
									class="rounded-lg bg-teal-600 py-3 px-6 font-medium text-white shadow transition-all duration-300 hover:bg-teal-700 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-offset-2 active:bg-teal-800 flex items-center justify-center group relative overflow-hidden"
									id="subscribeButton"
								>
								<span class="flex items-center justify-center">
									<!-- Default state -->
									<span class="flex items-center transition-transform group-hover:translate-x-1">
									<span>Subscribe</span>
									<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 ml-1 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
									</svg>
									</span>
									
									<!-- Loading state (initially hidden) -->
									<span class="absolute inset-0 flex items-center justify-center opacity-0" id="loadingState">
										<svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
											<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
											<path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
										</svg>
									</span>
								</span>
								</button>
							</div>
							
							<div class="flex items-start text-teal-600 text-sm">
								<input type="checkbox" id="privacy-consent" class="mr-2 mt-1 rounded-sm border border-teal-600" required />
								<label for="privacy-consent">I agree to receive emails and accept the <a href="#Agreement" class="underline hover:text-white">Privacy Policy</a></label>
							</div>
						</form>
						</div>
					</div>
				</div>
			{/if}
		</div>

		<!-- How It Works Preview -->
		{#if visible}
			<div class="mt-16" in:fly={{ y: 20, duration: 600, delay: 400 }}>
				<div class="text-center mb-8">
					<h2 class="text-2xl font-bold text-gray-800">How FutureSkills Coach Works</h2>
					<p class="mt-2 text-gray-600">Our three-step process guides you from assessment to action</p>
				</div>

				<div class="relative mx-auto max-w-7xl">
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
				</div>
				
				
				<div class="text-center mt-8">
					<a
						href="#how-it-works"
						class="inline-flex items-center px-6 py-3 rounded-lg bg-gradient-to-r from-green-600 to-teal-500 text-white font-medium shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<span>Get Started</span>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-5 w-5 ml-2"
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
			</div>
		{/if}
	</div>
</section>
<Footer />

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
	:global(.text-amber-100) {
		color: rgba(254, 243, 199, var(--tw-text-opacity, 1));
	}
	:global(.text-amber-200) {
		color: rgba(253, 230, 138, var(--tw-text-opacity, 1));
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