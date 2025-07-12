
st = {1, 2, 3}
print("Original set:", st)
st.add(4)
print("After add(4):", st)
st.remove(2)
print("After remove(2):", st)
st.discard(10)
print("After discard(10):", st)
removed = st.pop()
print("After pop():", st, "| Removed:", removed)
st.clear()
print("After clear():", st)
st.update([5, 6, 7])
print("After update([5, 6, 7]):", st)
st2 = {6, 7, 8, 9}
print("Second set:", st2)

print("Union:", st.union(st2))
print("Intersection:", st.intersection(st2))
