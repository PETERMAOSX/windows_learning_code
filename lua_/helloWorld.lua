--[[function function1(n)
	if n==0 then
		return 1
	else
		return n*function1(n-1)
	end
end
print(function1(5))
--]]
--[[a =5
local b = 5
function joke()
	c = 5
	local d = 6
end
joke ()
print (c,d)

do
	local a = 6
	b = 6
	print(a,b)
end


print(a,b)
--]]

a = 'hello' .. 'world'

print(a)
