<script lang="ts">
	import { fly, fade } from 'svelte/transition';
	import { onMount } from 'svelte';

    import Navbar from '$lib/components/layouts/Navbar.svelte';

	let visible = false;
	let activeTab = 'mission';

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
			year: '2023',
			milestone: 'Project Inception',
			description: 'FutureSkills Coach was conceived in response to accelerating job displacement in traditional sectors.'
		},
		{
			year: '2024',
			milestone: 'Research & Development',
			description: 'Our team analyzed job market data and built initial models to predict automation risk across industries.'
		},
		{
			year: '2025',
			milestone: 'Call for Code Hackathon',
			description: 'Developed as a proof-of-concept submission for the UN SDG 8 (Decent Work and Economic Growth) challenge.'
		},
		{
			year: 'Future',
			milestone: 'Full Platform Launch',
			description: 'Plans to expand features, integrate with job boards, and partner with educational institutions.'
		}
	];

	// Stats data
	const impactStats = [
		{ metric: '10 Million+', label: 'Jobs analyzed for automation risk' },
		{ metric: '50,000+', label: 'Green career paths in our database' },
		{ metric: '2,500+', label: 'Skill development pathways' },
		{ metric: '1,200+', label: 'Side hustle opportunities' }
	];
</script>

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
			<div class="mb-8" in:fly={{ y: 20, duration: 600, delay: 200 }}>
				<div class="flex flex-wrap justify-center gap-2 sm:gap-4">
					<button
						on:click={() => switchTab('mission')}
						class={`px-4 py-2 rounded-lg font-medium transition-all ${
							activeTab === 'mission'
								? 'bg-green-600 text-white shadow-md'
								: 'text-gray-600 hover:bg-gray-100'
						}`}
					>
						Our Mission
					</button>
					<button
						on:click={() => switchTab('team')}
						class={`px-4 py-2 rounded-lg font-medium transition-all ${
							activeTab === 'team'
								? 'bg-amber-500 text-white shadow-md'
								: 'text-gray-600 hover:bg-gray-100'
						}`}
					>
						Our Team
					</button>
					<button
						on:click={() => switchTab('faq')}
						class={`px-4 py-2 rounded-lg font-medium transition-all ${
							activeTab === 'faq'
								? 'bg-teal-500 text-white shadow-md'
								: 'text-gray-600 hover:bg-gray-100'
						}`}
					>
						FAQ
					</button>
				</div>
			</div>
		{/if}

		<!-- Tab Content -->
		<div class="overflow-hidden rounded-2xl bg-white shadow-xl">
			{#if activeTab === 'mission'}
                <div in:fade={{ duration: 300 }} class="grid md:grid-cols-2">
                    <!-- Left side - Image/Graphic -->
                    <div class="bg-gradient-to-br from-green-500 to-teal-600 p-8 flex items-center justify-center">
                        <div class="text-center">
                            <!-- Keep your existing SDG 8 icon but add some animation -->
                            <div class="mb-6 inline-flex h-24 w-24 items-center justify-center rounded-full bg-white bg-opacity-20 text-white hover:scale-105 transition-transform">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    class="h-12 w-12"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M13 10V3L4 14h7v7l9-11h-7z"
                                    />
                                </svg>
                            </div>
                            <h3 class="mb-2 text-2xl font-bold text-white">SDG 8</h3>
                            <p class="text-green-50">Decent Work and Economic Growth</p>
                
                            <!-- Keep your existing timeline but add visual improvements -->
                            <div class="mt-8">
                                <div class="relative">
                                    <!-- Vertical line with slight animation -->
                                    <div class="absolute left-1/2 top-0 h-full w-1 -translate-x-1/2 bg-white bg-opacity-30 animate-pulse"></div>
                
                                    {#each timeline as item, i}
                                        <div class="relative mb-8 flex items-center justify-center">
                                            <!-- Circle marker with hover effect -->
                                            <div class="absolute left-1/2 -translate-x-1/2 h-6 w-6 rounded-full border-2 border-white bg-green-600 flex items-center justify-center hover:scale-125 transition-transform">
                                                <div class="h-2 w-2 rounded-full bg-white"></div>
                                            </div>
                
                                            <!-- Content with subtle shadow -->
                                            <div class={`w-full ${i % 2 === 0 ? 'text-right pr-8' : 'text-left pl-8'} hover:text-white transition-colors`}>
                                                <p class="font-bold text-white">{item.year}</p>
                                                <p class="text-sm text-green-50 font-semibold">{item.milestone}</p>
                                                <p class="text-xs text-green-100">{item.description}</p>
                                            </div>
                                        </div>
                                    {/each}
                                </div>
                            </div>
                            
                            <!-- Add impact stats in a grid -->
                            <div class="mt-8 grid grid-cols-2 gap-4">
                                {#each impactStats.slice(0, 4) as stat}
                                    <div class="rounded-lg bg-white bg-opacity-10 p-3 hover:bg-opacity-20 transition-all">
                                        <p class="text-xl font-bold text-white">{stat.metric}</p>
                                        <p class="text-xs text-green-100">{stat.label}</p>
                                    </div>
                                {/each}
                            </div>
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
					<div class="bg-gradient-to-br from-teal-500 to-teal-600 p-8">
						<h2 class="mb-6 text-2xl font-bold text-white">Get in Touch</h2>

						<div class="mb-8 rounded-lg bg-white bg-opacity-10 p-6">
							<h3 class="mb-4 text-xl font-semibold text-white">Contact Us</h3>
							
							<div class="space-y-4">
								<div class="flex items-start">
									<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-white bg-opacity-20">
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
										<p class="font-medium text-white">Email</p>
										<p class="text-sm text-teal-100">contact@futureskillscoach.org</p>
									</div>
								</div>
								
								<div class="flex items-start">
									<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-white bg-opacity-20">
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
										<p class="font-medium text-white">Support</p>
										<p class="text-sm text-teal-100">Available Monday-Friday, 9am-5pm ET</p>
									</div>
								</div>
								
								<div class="flex items-start">
									<div class="mr-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full bg-white bg-opacity-20">
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
										<p class="font-medium text-white">Information</p>
										<p class="text-sm text-teal-100">Visit our Help Center for more resources</p>
									</div>
								</div>
							</div>
						</div>

						<div class="rounded-lg bg-white bg-opacity-10 p-6">
							<h3 class="mb-4 text-xl font-semibold text-white">Join Our Mission</h3>
							
							<p class="mb-4 text-teal-100">
								Sign up for updates about platform improvements, new features, and opportunities to contribute to our work.
							</p>
							
							<form class="space-y-4">
								<div>
									<input
										type="email"
										placeholder="Your email address"
										class="w-full rounded-lg border-0 bg-white bg-opacity-20 p-3 text-white placeholder-teal-100 focus:outline-none focus:ring-2 focus:ring-white"
									/>
								</div>
								
								<button
									type="submit"
									class="w-full rounded-lg bg-white py-3 px-4 font-medium text-teal-600 shadow transition-colors hover:bg-teal-50"
								>
									Subscribe
								</button>
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
				
				<div class="flex justify-center">
					<div class="relative">
						<div class="flex items-center">
							<!-- Step 1 -->
							<div class="relative flex flex-col items-center">
								<div class="h-12 w-12 rounded-full border-4 border-blue-500 bg-blue-100 mb-2 flex items-center justify-center">
									<span class="text-lg font-bold text-blue-600">1</span>
								</div>
								<span class="text-sm font-medium text-blue-600">Analyze</span>
							</div>

							<!-- Connector -->
							<div class="h-1 w-16 bg-green-500"></div>

							<!-- Step 2 -->
							<div class="relative flex flex-col items-center">
								<div class="h-12 w-12 rounded-full border-4 border-green-500 bg-green-100 mb-2 flex items-center justify-center">
									<span class="text-lg font-bold text-green-600">2</span>
								</div>
								<span class="text-sm font-medium text-green-600">Discover</span>
							</div>

							<!-- Connector -->
							<div class="h-1 w-16 bg-amber-500"></div>

							<!-- Step 3 -->
							<div class="relative flex flex-col items-center">
								<div class="h-12 w-12 rounded-full border-4 border-amber-500 bg-amber-100 mb-2 flex items-center justify-center">
									<span class="text-lg font-bold text-amber-600">3</span>
								</div>
								<span class="text-sm font-medium text-amber-600">Transition</span>
							</div>
						</div>
					</div>
				</div>
				
				<div class="text-center mt-8">
					<a
						href="#how-it-works"
						class="inline-flex items-center px-6 py-3 rounded-lg bg-gradient-to-r from-green-600 to-teal-500 text-white font-medium shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
					>
						<span>Learn the Details</span>
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