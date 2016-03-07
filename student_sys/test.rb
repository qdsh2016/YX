MR_COUNT = 0        # 定义在主 Object 类上的常量

module Foo
  MR_COUNT = 0
  ::MR_COUNT = 1    # 设置全局计数为 1
  MR_COUNT = 2      # 设置局部计数为 2
end

puts MR_COUNT       # 这是全局常量
puts Foo::MR_COUNT  # 这是 "Foo" 的局部常量 

if (1==2)
	puts 'ok'
end

def okk
	puts 'okk'
end

q=[1,2,3,4]
qq=Array.new(4) 


begin
	raise 'as'
rescue Exception , 'sd'
	
ensure 
	
end